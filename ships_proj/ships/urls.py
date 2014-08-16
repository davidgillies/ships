from django.conf.urls import patterns, url

from ships import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^other/$', views.other, name='other'), 
    url(r'^(?P<pk>\d+)/$', views.ShipDetailView.as_view(), name='ship detail'),
)
