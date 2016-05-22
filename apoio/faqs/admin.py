
from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'status', 'pub_date', 'user', 'answers', 'has_accepted_answer')
	search_fields = ('text',)

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('question', 'pub_date', 'user', 'accepted')
	search_fields = ('question.text', 'text')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
