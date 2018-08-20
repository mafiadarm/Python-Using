from django.contrib import admin

# Register your models here.

from .models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ["unumber", "uname", "upwd", "ustat"]


admin.site.register(UserInfo, UserInfoAdmin)