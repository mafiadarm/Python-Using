from django.db import models

# Create your models here.


class OrderStat(models.Model):
    # 单别
    order_type = models.CharField(max_length=4)
    # 单号
    order_number = models.CharField(max_length=11)
    # 品号
    pro_num = models.CharField(max_length=20)
    # 品名
    pro_name = models.CharField(max_length=80)
    # 单位
    unit = models.CharField(max_length=10, null=True)
    # 规格
    p_size = models.CharField(max_length=40, null=True)
    # 预计开工
    plan_start = models.CharField(max_length=8, null=True)
    # 预计完工
    plan_end = models.CharField(max_length=8, null=True)
    # 实际完工
    reality_time = models.CharField(max_length=8, null=True)
    # 状态码
    stat_code = models.CharField(max_length=1, null=True)
    # 批号
    batch = models.CharField(max_length=20, null=True)
    # 入库数量
    into_count = models.DecimalField(max_digits=12, decimal_places=2, null=True)
