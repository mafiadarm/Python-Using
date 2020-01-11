from django.http import HttpResponse
from django.shortcuts import redirect

from .models import UserInfo


def login(func):
    def login_func(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        user_name = request.session.get('user_name')
        find = UserInfo.objects.filter(id=user_id).first()
        if find:
            if find.stat == "1" and find.name == user_name:  # "1" is using
                return func(request, *args, **kwargs)
            else:
                return HttpResponse("THIS USERNAME BEING CLOSE")
        return redirect("/")
    return login_func
