# myfirstvis/urls.py
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    # re_path(r'^bar3d$', views.bar3),
]