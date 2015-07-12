from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brianverse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('frontpage.urls')),
    # url(r'^about/', include('about.urls')),
    # url(r'^event/', include('event.urls')),
    # url(r'^media/', include('media.urls')),
    # url(r'^store/', include('store.urls')),
)
