from django.conf.urls import url

from ships import views

urlpatterns = [
    url(r'^ships/$', views.Index.as_view(), name='index'),
    url(r'^other/$', views.other, name='other'), 
    url(r'^(?P<pk>\d+)/$', views.ShipDetailView.as_view(), name='ship detail'),
    url(r'^people/(?P<pk>\d+)/$', views.PeopleDetailView.as_view(), name='person_detail'),
    url(r'^ships/(?P<pk>\d+)/$', views.ShipDetailView.as_view()),
    url(r'^ships/create/$', views.ShipCreateView.as_view()),
    url(r'^ships/update/(?P<pk>\d+)/$', views.ShipUpdateView.as_view()),
    url(r'^ships/delete/(?P<pk>\d+)/$', views.ShipDeleteView.as_view()),
    url(r'^people/(?P<pk>\d+)/$', views.PeopleDetailView.as_view()),
    url(r'^people/create/$', views.PeopleCreateView.as_view()),
    url(r'^people/update/(?P<pk>\d+)/$', views.PeopleUpdateView.as_view()),
    url(r'^people/delete/(?P<pk>\d+)/$', views.PeopleDeleteView.as_view()),
    url(r'^builder/(?P<pk>\d+)/$', views.BuilderDetailView.as_view()),
    url(r'^builder/create/$', views.BuilderCreateView.as_view()),
    url(r'^builder/update/(?P<pk>\d+)/$', views.BuilderUpdateView.as_view()),
    url(r'^builder/delete/(?P<pk>\d+)/$', views.BuilderDeleteView.as_view()),

]
