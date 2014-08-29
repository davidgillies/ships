from django.conf.urls import patterns, url

from ships import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^other/$', views.other, name='other'), 
    url(r'^(?P<pk>\d+)/$', views.ShipDetailView.as_view(), name='ship detail'),
    url(r'^create/$', views.ShipCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', views.ShipUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', views.ShipDeleteView.as_view()),
)
