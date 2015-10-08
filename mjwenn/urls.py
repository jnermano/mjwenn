from django.conf.urls import patterns, include, url

from django.contrib import admin
import obgest

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mjwenn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('obgest.urls', namespace='obgest')),
)
