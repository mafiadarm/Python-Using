from django.http import HttpResponse
from django.shortcuts import redirect

from .models import UserInfo


def login(func):
    def login_func(request, *args, **kwargs):
        flag = request.session.get("user_id")
        find = UserInfo.objects.filter(unumber=flag)
        if flag and len(find) == 1:
            if find[0].ustat == "1":
                return func(request, *args, **kwargs)
            else:
                return HttpResponse("请联系管理员修改状态码")
        return redirect("/login/")
    return login_func
