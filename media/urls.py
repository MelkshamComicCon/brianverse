from django.conf.urls import patterns, url
from media import views

urlpatterns = patterns('',
	url(r'^$', 'media.views.media'),
	# url(r'^guests/$', 'event.views.guests'),
)