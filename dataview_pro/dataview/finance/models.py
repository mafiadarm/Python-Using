from django.db import models

# Create your models here.


class BalanceInfo(models.Model):
    # 编号
    bill_number = models.CharField(max_length=20)
    # 年
    close_year = models.CharField(max_length=4)
    # 月
    close_month = models.CharField(max_length=2)
    # 币种
    currency = models.CharField(max_length=10)
    # 来源码
    source_bill = models.CharField(max_length=4)
    # 部门
    department = models.CharField(max_length=8)
    # 本币(借)
    domestic_currency_borrow = models.DecimalField(decimal_places=2, max_digits=12)
    # 本币(贷)
    domestic_currency_loan = models.DecimalField(decimal_places=2, max_digits=12)
    # 未过账(借)
    uncleared_borrow = models.DecimalField(decimal_places=2, max_digits=12)
    # 未过账(贷)
    uncleared_loan = models.DecimalField(decimal_places=2, max_digits=12)


class DepartmentInfo(models.Model):
    # 编号
    depart_number = models.CharField(max_length=20)
    # 名称
    depart_name = models.CharField(max_length=40)
