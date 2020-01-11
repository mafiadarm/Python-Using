from django.db import models

# Create your models here.


class Number(models.Model):
    num = models.CharField(max_length=12)
    level = models.CharField(max_length=6, default='null')


class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=40)
    stat = models.CharField(max_length=2)
