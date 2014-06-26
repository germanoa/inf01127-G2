from django.conf.urls import patterns,url

from ipalloc import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^addnetwork/', views.add_network, name="addnetwork"),
    url(r'^adminmenu/', views.adminmenu, name="adminmenu"),
    url(r'^ip2manager/', views.ip2manager, name="ip2manager"),
    url(r'^ipdelmanager/', views.ipdelmanager, name="ipdelmanager"),
    url(r'^confsystem/', views.confsystem, name="confsystem")
)
