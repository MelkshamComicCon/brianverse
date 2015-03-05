from django.conf.urls import patterns, url
from event import views

urlpatterns = patterns('',
	url(r'^$', 'event.views.guests'),
	url(r'^guests/$', 'event.views.guests'),
)