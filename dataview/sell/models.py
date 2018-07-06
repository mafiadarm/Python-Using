from django.db import models

# Create your models here.


class SellProxyInfo(models.Model):
    # 年份
    sell_date = models.DateField(null=True)
    # 品号
    article = models.CharField(max_length=40, null=True)
    # 单位
    unit = models.CharField(max_length=100, null=True)
    # 单价
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)  #
    # 总价
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True)  #
    # 地址1
    add1 = models.CharField(max_length=100, null=True)
    # 地址2
    add2 = models.CharField(max_length=100, null=True)
    # 省份
    province = models.CharField(max_length=20, null=True)
    # 客户
    consumer = models.CharField(max_length=50, null=True)
    # 部门
    department = models.CharField(max_length=20, null=True)
    # 员工
    staff = models.CharField(max_length=20, null=True)


class SellDirectInfo(models.Model):
    # 年份
    sell_date = models.DateField(null=True)
    # 品号
    article = models.CharField(max_length=40, null=True)
    # 单位
    unit = models.CharField(max_length=100, null=True)
    # 单价
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    # 总价
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    # 地址1
    add1 = models.CharField(max_length=100, null=True)
    # 地址2
    add2 = models.CharField(max_length=100, null=True)
    # 省份
    province = models.CharField(max_length=20, null=True)
    # 代理商
    proxy = models.CharField(max_length=50, null=True)
    # 公司
    company = models.CharField(max_length=50, null=True)