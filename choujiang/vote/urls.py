from django.urls import path, re_path
from vote.views import *

app_name = 'toupiao'
urlpatterns = [
    path('choose/', vote_index, name='vote_index'),
    path('score/', make_score, name='score'),
    path('get_score/', get_score, name='get_score'),
    path('bar/', bar, name='bar'),
    path('view/', view, name='to_view'),
    ]
