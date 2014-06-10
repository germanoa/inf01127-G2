from django.conf.urls import patterns,url

from ipalloc import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^addnetwork/', views.add_network, name="addnetwork"),
    url(r'^select_manager_to_network/', views.select_manager_to_network, name="select_manager_to_network"),
    url(r'^adminmenu/', views.adminmenu, name="adminmenu")
)
