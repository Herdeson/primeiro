from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'primeiro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^identifica/', include('Identifica.urls', namespace="identifica")),
    #url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
]
