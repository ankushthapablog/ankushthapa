from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('homepage.views',
    # Examples:
    url(r'^$','homepage', name='homepage'),
)
