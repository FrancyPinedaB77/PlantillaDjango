from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^taller2$', views.index, name='index'),
 	url(r'^$', views.inicio),
 	url(r'^grafo$', views.grafo, name='mygraph'),
 	url(r'^Taller3$', views.taller3, name='taller3'),
	]
