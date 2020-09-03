from django.conf.urls import url
from .views import home, account

urlpatterns = [
    url(r'^orm$', home.orm),
    url(r'^login$', account.login),
    url(r'^register$', account.register),
    url(r'^check_code$', account.check_code),
    url(r'^(?P<site>\w+).html', home.home),
    url(r'^(?P<site>\w+)/(?P<condition>((tag)|(date)|(category)))/(?P<val>\w+-*\w+).html', home.filter),
    url(r'^all/(?P<article_type_id>\d+).html$', home.index, name='index'),
    url(r'^(?P<site>\w+)/(?P<nid>\d+).html', home.detail),
    url(r'^logout.html$', account.logout),
    url(r'^jsonp.html$', account.jsonp),
    url(r'^', home.index),
]
