from django.conf.urls import patterns,url

from ipalloc import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^addnetwork/', views.add_network, name="addnetwork"),
    url(r'^adminmenu/', views.adminmenu, name="adminmenu")
)
