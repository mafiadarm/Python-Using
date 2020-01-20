from django.contrib import admin
from .models import Tag, Votes, Start, People


# Register your models here.

@admin.register(Votes)
class VotesAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduce', 'score')
    search_fields = ['name', 'tags']
    list_per_page = 20


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('user_ip', 'from_host', 'visits_url', 'target', 'come_time')


class TagAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ["name"]


class StartAdmin(admin.ModelAdmin):
    list_display = ["flag"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Start, StartAdmin)
