from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'iptools.views.index', name='index'),
    url(r'^login/', 'iptools.views.login', name='login'),
    url(r'^logout/', 'iptools.views.logout', name='logout'),
    url(r'^dashboard/', 'iptools.views.dashboard', name='dashboard'),
    url(r'^ipalloc/', include('ipalloc.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
