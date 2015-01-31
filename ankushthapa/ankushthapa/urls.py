from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.homepage'),
    url(r'^twitter/$', 'homepage.views.twitter'),
    url(r'^instagram/$', 'homepage.views.instagram'),
    url(r'^admin/', include(admin.site.urls)),
)
