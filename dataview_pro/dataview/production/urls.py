from django.urls import re_path
from . import views

urlpatterns = [

    re_path(r'^$', views.index),
    re_path(r'^buy_history_date/$', views.buy_history_date),
    re_path(r'^buy_history_price/$', views.buy_history_price),
    re_path(r'^usual_deal_amount_rank/$', views.usual_deal_amount_rank),
    re_path(r'^usual_deal_adeal_rank/$', views.usual_deal_adeal_rank),
    re_path(r'^usual_deal_money_rank/$', views.usual_deal_money_rank),


]
