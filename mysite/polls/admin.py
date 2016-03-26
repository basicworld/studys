from django.contrib import admin

# Register your models here.
# wlf: set Question to admin page
from .models import Question, Choice

# wlf: show choices -- solution 2
class ChoiceInline(admin.TabularInline):
    """
    wlf: use for showing choices in Qustion view
    child class admin.StackedInline will take alot space in web page
    child class admin.TabularInline takes less space
    """
    model = Choice
    extra = 1 # show how many black_choices by default 

# wlf: chango admin view
class QuestionAdmin(admin.ModelAdmin):
    # wlf: change order of question detail in admin
    fields = ['question_text', 'pub_date',]
    inlines = [ChoiceInline]

    # # wlf: split form
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    # wlf: chage question list page 
    list_display = ('id','question_text', 'pub_date', 'was_published_recently')

    # wlf: add filter sidebar
    list_filter = ['pub_date']

    # wlf: add search capability
    search_fields = ['question_text']

# wlf: register it so we can see the model in admin page
admin.site.register(Question, QuestionAdmin)

# # wlf: show choices -- solution 1
# # wlf: this is not a good way to show choices
# admin.site.register(Choice)


