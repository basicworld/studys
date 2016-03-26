from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question, Choice
from .views import IndexView
from django.core.urlresolvers import reverse
# wlf: test
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose 
        pub_date is in the future
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose 
        pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)

        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)

        self.assertEqual(recent_question.was_published_recently(), True)

class ViewsMethodTests(TestCase):

    def test_get_queryset(self):
        """
        IndexView.get_queryset() should return question lists whose pub_date is 
        smaller than now
        """
        app = IndexView()
        question_list = app.get_queryset()
        for question in question_list:
            self.assertEqual(question.pub_date<=timezone.now(), True)

def create_question(question_text, days, create_choice=True):
    """
    Creates a question with the given `question_text` and published the given
    number of `days` offset to now (negative for questions publisehd in the 
        past, positive for qeustions that yet to be publisehd)
    @days=-30 30days ago from now
    @create_choice=True question with a choice
    @create_choice=False question with no choices

    """

    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=time)
    if create_choice:
        question.choice_set.create(choice_text="Choice 1", votes=0)
    return question

class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], 
            [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the index 
        page
        """
        create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], 
            ['<Question: Past question>'])

    def test_index_view_with_future_question_and_past_question(self):
        """
        only past questions should be displayed
        """
        create_question(question_text="Past question", days=-30)
        create_question(question_text="Future qeustion", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
            ['<Question: Past question>'])

    def test_index_view_with_two_past_questions(self):
        """
        The qeustions index page may display multiple questions
        """
        create_question(question_text="Past question 1", days=-30)
        create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], 
            ['<Question: Past question 2>', '<Question: Past question 1>'])

class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found
        """
        future_question = create_question(question_text="Future question", 
            days=5)
        response = self.client.get(reverse('polls:detail', 
            args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail of a question with a pub_date in the past should display
        the qeustion's text
        """
        past_question = create_question(question_text="Past question", 
            days=-30)

        response = self.client.get(reverse('polls:detail', 
            args=(past_question.id,)))
        
        self.assertContains(response, past_question.question_text, 
            status_code=200)

class PollsViewsVoteTests(TestCase):
    def test_vote_view_with_a_past_question(self):
        """
        if there is a past question, it should be displayed
        """
        past_question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:vote', 
            args=(past_question.id,)))
        self.assertContains(response, past_question.question_text, 
            status_code=200)

    def test_vote_view_with_a_future_question(self):
        """
        if there is a future qeustion, it shouldn't be displayed
        """
        future_question = create_question(question_text="Future question", 
            days=30)
        response = self.client.get(reverse('polls:vote', 
            args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_vote_view_with_question_which_has_no_choices(self):
        """
        a question without choices should not be displayed
        """
        past_question_without_choices = create_question(question_text="Test \
            question without choices", days=-30, create_choice=False)
        response = self.client.get(reverse('polls:vote', 
            args=(past_question_without_choices.id,)))
        self.assertEqual(response.status_code, 404)

    def test_vote_view_with_qeustion_which_has_choices(self):
        """
        a qeustion with choices should be displayed
        """
        past_question_with_choices = create_question(question_text="Test \
            question with one choice", days=-30, create_choice=True)
        response = self.client.get(reverse('polls:vote', \
            args=(past_question_with_choices.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question_with_choices.question_text,\
            status_code=200)