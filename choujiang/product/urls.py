from django.urls import path
from product.views import index, right_num, level_three, level_two, right_ten, congratulations

app_name = 'choujiang'
urlpatterns = [
    path('1/', index),
    path('2/', level_two, name='level2'),
    path('3/', level_three, name='level3'),
    path('c/', congratulations, name='c'),

    path('szPEZb/', right_num, name='right_num'),
    path('eBxdaE/', right_ten, name='right_ten'),
    ]
