from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


    # the 'name' value as called by the {% url %} template tag
    # name serve para utilizar no template para nao ter acomplamento com o layout
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]