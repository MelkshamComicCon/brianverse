from django.conf.urls import patterns, url
from store import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'))