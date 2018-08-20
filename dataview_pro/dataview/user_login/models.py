from django.db import models

# Create your models here.


class UserInfo(models.Model):
    unumber = models.CharField(max_length=7)
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    ustat = models.CharField(max_length=2)
