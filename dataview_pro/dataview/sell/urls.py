from django.urls import re_path
from . import views

urlpatterns = [

    re_path(r'^$', views.index),

    re_path(r'^direct/$', views.direct_index),
    re_path(r'^direct_rank/$', views.direct_ranking),
    re_path(r'^direct_record/$', views.direct_customer_record),
    re_path(r'^direct_record_10/$', views.direct_customer_record_ten),

    re_path(r'^direct_staff_rank/$', views.direct_staff_ranking),
    re_path(r'^direct_staff_record/$', views.direct_staff_record),
    re_path(r'^direct_staff_record_10/$', views.direct_staff_record_ten),

    re_path(r'^direct_depart_rank/$', views.direct_depart_ranking),
    re_path(r'^direct_depart_record/$', views.direct_depart_record),

    re_path(r'^proxy/$', views.proxy_index),
    re_path(r'^proxy_rank/$', views.proxy_ranking),
    re_path(r'^proxy_record/$', views.proxy_customer_record),
    re_path(r'^proxy_record_10/$', views.proxy_customer_record_ten),

    re_path(r'^proxy_client_rank/$', views.proxy_client_ranking),
    re_path(r'^proxy_client_record/$', views.proxy_client_customer_record),
    re_path(r'^proxy_client_record_10/$', views.proxy_client_customer_record_ten),

    re_path(r'^product_ratio/$', views.product_ratio),
    re_path(r'^product_ratio_direct/$', views.product_ratio_direct),
    re_path(r'^product_ratio_proxy/$', views.product_ratio_proxy),

    re_path(r'^product_ranking/$', views.product_ranking),
    re_path(r'^product_pile/$', views.product_pile),
    re_path(r'^product_record/$', views.product_record),


]
