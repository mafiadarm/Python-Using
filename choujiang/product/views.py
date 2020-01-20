import json
import random
from hashlib import md5
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse

from .models import Number
from .models import UserInfo
from .user_decorator import login


# Create your views here.

def creat_num(level):
    # creat the number
    flag = 1
    v = ''
    while flag:
        k = random.randint(1, 1000)
        v = "000" + "{:04d}".format(k)
        if not Number.objects.filter(num=v).count():
            flag = 0

    # recode
    new_num = Number()
    new_num.num = v
    new_num.level = level
    new_num.save()

    return v


@login
def right_num(request):
    v = creat_num('一等奖')
    return HttpResponse(v)


@login
def right_ten(request):
    vs = []
    level = request.GET['level']
    for _ in range(10):
        k = creat_num(level)
        vs.append(k)
    return HttpResponse(json.dumps(vs))


@login
def level_one(request):
    """get one"""
    content = {'jiangpiaohaoma': '2020大吉大利', 'level': '一等奖'}
    return render(request, 'level1.html', content)


@login
def level_two(request, how):
    how = int(how) if how else 6
    content = {'level': '二等奖', "how": range(how), "split": 3}
    return render(request, 'base_23.html', content)


@login
def level_three(request, how):
    how = int(how) if how else 10
    content = {'level': '三等奖', "how": range(how), "split": 5}
    return render(request, 'base_23.html', content)


@login
def choose(requset):
    return render(requset, 'choose.html')


def congratulations(request):
    one = Number.objects.filter(level='一等奖').values_list('num').order_by('num')[:2]
    two = Number.objects.filter(level='二等奖').values_list('num').order_by('num')[:6]
    thr = Number.objects.filter(level='三等奖').values_list('num').order_by('num')[:30]
    one_name = [i[0] for i in one]
    two_name = [i[0] for i in two]
    thr_name = [i[0] for i in thr]
    content = {'one': one_name, 'two': two_name, 'thr': thr_name}
    return render(request, 'congratulations.html', content)


def index(request):
    return render(request, "index.html")


def login_handle(request):
    post = request.POST
    name = post.get("user_name", None)
    pwd = post.get("pwd", None)

    users = UserInfo.objects.filter(name=name).first()  # []

    if users:
        # ---验证---
        my_pwd = md5(pwd.encode()).hexdigest()
        if my_pwd == users.pwd:
            request.session["user_id"] = users.id
            request.session["user_name"] = users.name
            request.session.set_expiry(0)
            # return HttpResponseRedirect("/2/")  # to choose level
            return HttpResponseRedirect('/o/')
        # ---验证---
        else:
            context = {"title": "user login", "error_name": 0, "error_pwd": 1, "name": name, "wpd": pwd, }
    else:
        context = {"title": "user login", "error_name": 1, "error_pwd": 1, "name": name, "wpd": pwd, }

    return render(request, "login.html", context)


def make_pwd(pwd):
    return md5(pwd.encode()).hexdigest()


if __name__ == '__main__':
    print(make_pwd('w9cmafia'))
