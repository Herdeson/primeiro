from django.conf.urls import url

from . import views

urlpatterns = [
	
    #url(r'^$', views.teste, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^individuo/add/$', views.IndividuoCreate.as_view(), name='individuo_add')
    # the 'name' value as called by the {% url %} template tag
    # name serve para utilizar no template para nao ter acomplamento com o layout
    #url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
   
]