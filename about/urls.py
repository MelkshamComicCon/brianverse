from django.conf.urls import patterns, url
# from about import views

urlpatterns = patterns('',
	url(r'^$', 'about.views.about'),
	url(r'^brians/$', 'about.views.brians'),
)