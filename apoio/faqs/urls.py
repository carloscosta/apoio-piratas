from django.conf.urls import url
from . import views


urlpatterns = [
        ## /faqs/ the timely ordered list of approved questions
        url(r'^$', views.index, name='index'),

        ## /faqs/$question_id/ the question id, visible if pending and not-answered
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

        ## /faqs/$question_id/results/ the question id, visible if aproved and answered
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

        ## /faqs/$question_id/vote/ the question id, visible on any state and been it answered or not
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

