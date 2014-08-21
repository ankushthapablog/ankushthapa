from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('homepage.views',
    # Examples:
    url(r'^$','homepage', name='homepage'),
    url(r'^/(.*)',RedirectView.as_view(url='/')),
)
