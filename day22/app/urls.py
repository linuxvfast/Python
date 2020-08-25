from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url('^index/$', views.index),
    url(r'^logout/$', views.logout),
    # url(r'^test/(?P<nid>\d+)$', views.test),
    url(r'^cache/$', views.cache),
    url(r'^signal/$', views.signal),
    url(r'^fm/$', views.fm),
]
