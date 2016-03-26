# wlf: connect to datebase: sqlite by default
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# @python_2_unicode_compatible
class Question(models.Model):
    """
    All model is a python class that subclasses django.db.models.Model
    @question_text
    @pub_date each attribute of model represent a database field
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        # wlf: fix future_time bug
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date > timezone.now() - datetime.timedelta(days=1)

    # wlf: add attributes to was_published_recently, so that we can sort it \
    # in admin page
    was_published_recently.admin_order_field = 'pub_date' # for ordering
    was_published_recently.boolean = True # change True/Flase to small symbol
    was_published_recently.short_description = 'Published recently?'



# @python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text