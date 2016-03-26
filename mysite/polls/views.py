from django.shortcuts import render
from django.shortcuts import get_object_or_404
# wlf: for web page
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.core.urlresolvers import reverse

from django.views import generic
from django.utils import timezone


# # wlf: loader is for: use template, not use render
# from django.template import loader
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # wlf: pub_date__lte: means pub_date less than or equal to ...
        return Question.objects.filter(pub_date__lte=timezone.now(), pk__in=\
            [x.question.pk for x in Choice.objects.all()])\
            .order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now(), pk__in=\
            [x.question.pk for x in Choice.objects.all()])

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    def get_queryset(self):
        """
        excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now(), pk__in=\
            [x.question.pk for x in Choice.objects.all()])


# def index(request):
#     # return HttpResponse("hello, you're at the polls index")
#     latest_question_list = Question.objects.filter\
        #(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

#     # # wlf: not use template
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

#     # # wlf: use template, not use render
#     # template = loader.get_template('polls/index.html')
#     # content = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(content, request))

#     # wlf: use template, render
#     content = {
#         'latest_question_list': latest_question_list,

#     }
#     return render(request, 'polls/index.html', content)

# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # # wlf: not use get_objects_or_404
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question,})

#     # wlf: use get_objects_or_404: it will use the Question.objects.get() func,
#     # btw get_list_or_404 will use Question.objects.filter() func
#     question = get_object_or_404(Question, pk=question_id)
#     content = {
#         'question': question,
#     }
#     return render(request, 'polls/detail.html', content)


# def results(request, question_id):
#     # response = "You're looking at the results of questions %s." 
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     content = {
#         'question': question,
#     }
#     return render(request, 'polls/results.html', content)

def vote(request, question_id):

    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id, pub_date__lte=\
        timezone.now(), pk__in=[x.question.pk for x in Choice.objects.all()])
    # .filter(pub_date__lte=timezone.now())

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        content = {
            'question': question,
            'error_message': "You didn't select a choice",
        }
        return render(request, 'polls/detail.html', content)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', 
            args=(question.id,)))