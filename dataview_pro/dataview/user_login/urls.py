from django.urls import re_path
from . import views

urlpatterns = [

    re_path(r'^$', views.login),
    re_path(r'^login/$', views.login_handle),
    re_path(r'^logout/$', views.logout),

]