from django.contrib import admin
from .models import Number

# Register your models here.


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ("num", 'level')
    search_fields = ["num"]
    list_per_page = 100