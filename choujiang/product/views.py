import json

from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Number


# Create your views here.

def creat_num(level):
    # creat the number
    flag = 1
    v = ''
    while flag:
        k = random.randint(1, 9999999)
        v = "{:07d}".format(k)
        if not Number.objects.filter(num=v).count():
            flag = 0

    # recode
    new_num = Number()
    new_num.num = v
    new_num.level = level
    new_num.save()

    return v


def index(request):
    """get one"""
    content = {'jiangpiaohaoma': '2020大吉大利', 'level': '一等奖'}
    return render(request, 'level1.html', content)


def right_num(request):
    v = creat_num('一等奖')
    return HttpResponse(v)


def right_ten(request):
    vs = []
    level = request.GET['level']
    for _ in range(10):
        k = creat_num(level)
        vs.append(k)
    return HttpResponse(json.dumps(vs))


def level_two(request):
    content = {'level': '二等奖'}
    return render(request, 'base_23.html', content)


def level_three(request):
    content = {'level': '三等奖'}
    return render(request, 'base_23.html', content)


def congratulations(request):
    one = Number.objects.filter(level='一等奖').values_list('num').order_by('num')[:2]
    two = Number.objects.filter(level='二等奖').values_list('num').order_by('num')[:10]
    thr = Number.objects.filter(level='三等奖').values_list('num').order_by('num')[:20]
    one_name = [i[0] for i in one]
    two_name = [i[0] for i in two]
    thr_name = [i[0] for i in thr]
    content = {'one': one_name, 'two': two_name, 'thr': thr_name}
    return render(request, 'congratulations.html', content)
