from django.conf.urls import include, url
from django.contrib import admin
from polls import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'primeiro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    #url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
]
