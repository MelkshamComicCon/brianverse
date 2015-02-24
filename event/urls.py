from django.conf.urls import patterns, url
from event import views

urlpatterns = patterns('',
	url(r'^$', 'event.views.event'),
	# url(r'^guests/$', 'event.views.guests'),
)