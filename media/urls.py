from django.conf.urls import patterns, url
from media import views

urlpatterns = patterns('',
	url(r'^$', 'media.views.gallery'),
	# url(r'^gallery/$', 'media.views.gallery'),
)