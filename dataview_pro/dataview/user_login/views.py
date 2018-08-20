from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import UserInfo
from hashlib import md5
from .user_decorator import login


# Create your views here.
def index(request):
    return redirect("/sell/")


def register(request):
    return render(request, 'user/register.html')


def register_handle(request):
    post = request.POST
    unumber = post["user_number"]
    uname = post["user_name"]
    upwd = post["pwd"]
    upwd2 = post["cpwd"]

    count = UserInfo.objects.filter(unumber=unumber).count()

    if not unumber or upwd != upwd2 or count >= 1:
        return redirect("/register/")

    user = UserInfo()
    user.unumber = unumber
    user.uname = uname
    user.upwd = md5(upwd.encode()).hexdigest()
    user.save()

    return redirect("/login/")


@login
def edit(request):
    return render(request, 'user/edit.html')


def edit_handle(request):
    unumber = request.session.get("user_id")

    post = request.POST
    upwd = post["pwd"]
    upwd2 = post["cpwd"]

    user = UserInfo.objects.get(unumber=unumber)

    if upwd != upwd2:
        return HttpResponse("两次密码输入不一样")
    if not user:
        return HttpResponse("账号错误")

    user.upwd = md5(upwd.encode()).hexdigest()
    user.save()

    return redirect("/sell/")


# def register_exist(request):
#     uname = request.GET.get("uname")
#     count = UserInfo.objects.filter(uname=uname).count()
#     print(count)
#     return JsonResponse({"count": count})


def login(request):
    uname = request.COOKIES.get("uname", "")
    context = {"title": "user login", "error_name": 0, "error_pwd": 0, "uname": uname}
    return render(request, "user/login.html", context)


def login_handle(request):
    post = request.POST
    unumber = post.get("usernumber")
    upwd = post.get("pwd")

    users = UserInfo.objects.filter(unumber=unumber)  # []

    if len(users) == 1:
        my_pwd = md5(upwd.encode()).hexdigest()
        if my_pwd == users[0].upwd:
            correct = HttpResponseRedirect("/sell/")

            request.session["user_id"] = users[0].unumber
            request.session["user_name"] = users[0].uname
            return correct
        else:
            context = {"title": "user login", "error_name": 0, "error_pwd": 1, "uname": unumber, "uwpd": upwd, }
    else:
        context = {"title": "user login", "error_name": 1, "error_pwd": 1, "uname": unumber, "uwpd": upwd, }

    return render(request, "user/login.html", context)


def logout(request):
    request.session.flush()
    return redirect("/login/")

