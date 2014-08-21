from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'homepage.views.homepage'),
    #url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'homepage.views.redirecter'
