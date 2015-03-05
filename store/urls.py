from django.conf.urls import patterns, url
from event import views

urlpatterns = patterns('',
	url(r'^$', 'store.views.store'),
	url(r'^store/$', 'store.views.store'),
)