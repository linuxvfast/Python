from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orm$', views.orm),
    url(r'^index$', views.index),
    url(r'^user_list/$', views.user_list),
    url(r'^edit-(\d+)/$', views.user_edit),
    url(r'^ajax$', views.ajax),
    url(r'^ajax_json/$', views.ajax_json),
    url(r'^upload/$', views.upload),
    url(r'^upload_file/$', views.upload_file),
    url(r'^kind/$', views.kind),
    url(r'^upload_img/$', views.upload_img),
    url(r'^file_manager/$', views.file_manager),
    url(r'^req$', views.req),
    url(r'^article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html', views.article, name='article'),
]
