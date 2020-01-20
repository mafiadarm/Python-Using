from django.urls import path, re_path
from product.views import *

app_name = 'choujiang'
urlpatterns = [
    path('1/', level_one, name='level1'),
    re_path('^2/(?P<how>\d)?', level_two, name='level2'),
    re_path('^3/(?P<how>\d)?', level_three, name='level3'),
    path('c/', congratulations, name='c'),
    path('o/', choose, name='choose'),

    path('szPEZb/', right_num, name='right_num'),
    path('eBxdaE/', right_ten, name='right_ten'),

    re_path(r'^login/$', login),
    re_path(r'^l/$', login_handle, name='login_verify'),
    re_path(r'', index, name='index'),
    ]
