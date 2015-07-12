from django.conf.urls import patterns, url
# from frontpage import views

urlpatterns = patterns('',
	url(r'^$', 'frontpage.views.home'),
)