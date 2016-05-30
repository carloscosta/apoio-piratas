from django.conf.urls import url
from . import views


app_name = 'faqs'
urlpatterns = [
        ## /faqs/ the timely ordered list of approved questions
        url(r'^$', views.index, name='index'),

        ## /faqs/$question_id/ the question id, visible if pending and not-answered
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

        ## /faqs/$question_id/results/ the question id, visible if aproved and answered
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

        ## /faqs/$question_id/ask/ the question id, form to ask a question
        url(r'^ask/$', views.ask, name='ask'),
]

