from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'ships_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'ships.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ships.urls')),
]
