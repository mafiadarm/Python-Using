from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import UserInfo
from hashlib import md5


# Create your views here.


def login(request):
    uname = request.COOKIES.get("uname", "")
    context = {"title": "user login", "error_name": 0, "error_pwd": 0, "uname": uname}
    return render(request, "user/login.html", context)


def login_handle(request):
    post = request.POST
    uname = post.get("username")
    upwd = post.get("pwd")

    users = UserInfo.objects.filter(uname=uname)  # []

    if len(users) == 1:
        print("user login")
        my_pwd = md5(upwd.encode()).hexdigest()
        if my_pwd == users[0].upwd:
            correct = HttpResponseRedirect("/sell/")

            request.session["user_id"] = users[0].id
            request.session["user_name"] = uname
            return correct
        else:
            context = {"title": "user login", "error_name": 0, "error_pwd": 1, "uname": uname, "uwpd": upwd, }
    else:
        context = {"title": "user login", "error_name": 1, "error_pwd": 1, "uname": uname, "uwpd": upwd, }
    return render(request, "user/login.html", context)


def logout(request):
    request.session.flush()
    return redirect("/")

