from django.conf.urls import patterns, url

from ships import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^other/$', views.other, name='other'), 
)
