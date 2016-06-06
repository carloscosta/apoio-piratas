from django.conf.urls import url
from . import views


app_name = 'faqs'
urlpatterns = [
        ## /faqs/ the timely ordered list of approved questions
        url(r'^$', views.index, name='index'),

        ## /faqs/$question_id/ the question id, visible if pending and not-answered
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

        ## /faqs/ask/ form to ask a question
        url(r'^ask/$', views.ask, name='ask'),

        ## /faqs/ask/ The thanks page after submitted throw ask a question
        url(r'^ask/thanks/$', views.thanks, name='thanks'),
]

