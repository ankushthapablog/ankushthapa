from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.homepage'),
    url(r'^admin/', include(admin.site.urls)),
)
