from django.contrib import admin
from .models import Number
from .models import UserInfo

# Register your models here.


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ("num", 'level')
    search_fields = ["num"]
    list_per_page = 100


class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ["name", "pwd", "stat"]


admin.site.register(UserInfo, UserInfoAdmin)
