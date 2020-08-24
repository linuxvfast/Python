from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^user_list/', views.user_list),
]
