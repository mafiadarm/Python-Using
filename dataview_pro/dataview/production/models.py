from django.db import models

# Create your models here.


# 采购信息
class ProcurementInfo(models.Model):
    # 日期
    pro_date = models.DateField(null=True)
    # 品名
    article = models.CharField(max_length=40, null=True)
    # 品号
    art_num = models.CharField(max_length=20, null=True)
    # 规格
    art_size = models.CharField(max_length=100, null=True)
    # 单位
    unit = models.CharField(max_length=100, null=True)
    # 数量
    amount = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    # 单价
    price = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    # 总价 开票金额
    total_price = models.DecimalField(max_digits=12, decimal_places=4, null=True)
