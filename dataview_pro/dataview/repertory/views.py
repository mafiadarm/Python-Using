from django.shortcuts import render
from .models import OrderStat

# Create your views here.


def index(request):
    spi = OrderStat.objects.values().order_by("stat_code")
    code_dict = {"Y": "完工", "1": "未生产", "2": "已领料", "3": "生产中", "y": "手动结束", "": ""}
    for i in spi:
        i["plan_start"] = i["plan_start"][:4] + "-" + i["plan_start"][4:6] + "-" + i["plan_start"][6:8]
        i["plan_end"] = i["plan_end"][:4] + "-" + i["plan_end"][4:6] + "-" + i["plan_end"][6:8]
        i["reality_time"] = i["reality_time"][:4] + "-" + i["reality_time"][4:6] + "-" + i["reality_time"][6:8]
        i["stat_code"] = code_dict[i["stat_code"]]

    context = dict(
        orders=spi
    )
    return render(request, "repertory/order_stat.html", context=context)

