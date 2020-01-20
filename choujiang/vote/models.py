from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Votes(models.Model):
    name = models.CharField('节目名称', max_length=50, default='null')
    introduce = models.TextField('节目介绍', default='null')
    score = models.IntegerField('得分', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)


class People(models.Model):
    user_ip = models.GenericIPAddressField("用户")
    from_host = models.CharField("远程地址", max_length=20)
    visits_url = models.TextField("访问url")
    target = models.CharField('打分对象', max_length=50, default='null')
    come_time = models.DateTimeField(auto_now_add=True)


class Start(models.Model):
    flag = models.IntegerField('start/stop', default=0)
