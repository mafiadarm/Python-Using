import datetime
from collections import Counter

from django.shortcuts import render
from pyecharts import Bar, Bar3D

from .models import ProcurementInfo

# Create your views here.
"""
进产存--->
    采购品历史价格
    生产单缺货情况
    生产单进度
    生产排程数量
    库存量
    库存排名
        成品
        半成品
        原材料
    库存品进出量
    关键原材料库存比
    成品库存比/警戒值
"""


def choice_object():
    date = ProcurementInfo.objects.values_list("pro_date", flat=True)
    date = sorted({str(i)[:4] for i in date})

    num_name = ProcurementInfo.objects.values_list("art_num", "article")
    num_name = set(num_name)
    num_name = sorted(num_name, key=lambda x: x[0])
    num_name = [" ".join(i) for i in num_name]
    return date, num_name


def view_bar_3D(x_list, y_list, data_list, name):
    """
    需要数据
    self.x_list 12个月的月份[日期] 等...
    self.y_list 各个不同的年份 等...
    self.date_list [[x, y, v], [x, y, v]] x和y是坐标索引，从0开始计算，v是展示的值
    :return:
    """
    bar3d = Bar3D(name + "汇总表", width=1000, height=500)
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    # print(x_list, y_list, data_list)
    bar3d.add("", x_list, y_list, data_list,
              is_visualmap=True,
              visual_range=[0, int(max(data_list, key=lambda x: x[2])[2])],
              visual_range_color=range_color,
              grid3d_width=200,
              grid3d_depth=80,
              is_toolbox_show=False,
              grid3d_shading='lambert',
              is_grid3d_rotate=True,
              )

    return bar3d.render_embed()


def index(request):
    value_dict = {}

    spi = ProcurementInfo.objects.values_list("pro_date", "total_price")
    year = ProcurementInfo.objects.values_list("pro_date", flat=True)
    y_list = sorted(set([str(i)[:4] for i in year]))

    for dat, tot in spi:

        ym = str(dat)[:7]

        if ym in value_dict:
            value_dict[ym] += int(tot)
        else:
            value_dict[ym] = int(tot)

    data_list = [[int(k[5:7]) - 1, int(k[:4]) - 2015, int(v)] for k, v in value_dict.items()]
    x_list = ["{}月".format(i) for i in range(1, 13)]

    pattern = view_bar_3D(x_list, y_list, data_list, "采购")

    context = dict(
        myechart=pattern,
    )

    return render(request, "production/index.html", context=context)


# 柱状图[区域]
def datazoom(spi, year, name):
    if not name:
        return "请选择具体名称！"
    if year:
        start_date = datetime.date(int(year), 1, 1)
    else:
        start_date = datetime.date(2015, 1, 1)
    day_plus = datetime.timedelta(days=1)
    end_date = datetime.date.today()

    day_list = []
    while start_date <= end_date:
        day_list.append(start_date)
        start_date += day_plus

    value_list = [0] * len(day_list)
    for i in spi:
        value_list[day_list.index(i[0])] = float(i[1])

    barzoom = Bar()
    barzoom.add(name + " " + year + " 交易概况", day_list, value_list,
                is_datazoom_show=True, datazoom_type="both", xaxis_rotate=0, datazoom_range=[0, 100])
    return barzoom.render_embed()


# 交易历史日期查询
def buy_history_date(request):
    pattern = ""
    choice_year = ""
    choice_name = ""

    if request.method == "POST":
        choice_year = request.POST["year"]
        choice_name = request.POST["name"]
        if choice_name:
            choice_numb, choice_name = choice_name.split(" ")

            data_list = ProcurementInfo.objects.filter(art_num=choice_numb).values_list("pro_date", "total_price")
            pattern = datazoom(data_list, choice_year, choice_name)

    date, num_name = choice_object()

    context = dict(
        myechart=pattern,
        consumer=num_name,
        sell_date=date,
        date_year=choice_year,
        consumer_name=choice_name,
    )
    return render(request, "production/rank.html", context=context)


# 交易历史单价查询
def buy_history_price(request):
    pattern = ""
    choice_year = ""
    choice_name = ""

    date, num_name = choice_object()

    if request.method == "POST":
        choice_year = request.POST["year"]
        choice_name = request.POST["name"]
        if choice_name:
            choice_numb, choice_name = choice_name.split(" ")

            data_list = ProcurementInfo.objects.filter(art_num=choice_numb).values_list("pro_date", "price")
            pattern = datazoom(data_list, choice_year, choice_name)

    context = dict(
        myechart=pattern,
        consumer=num_name,
        sell_date=date,
        date_year=choice_year,
        consumer_name=choice_name,
    )
    return render(request, "production/rank.html", context=context)


def rank_bar(name_list, value_list, title):
    bar_page = Bar()
    bar_page.add(title + "排名", name_list, value_list, xaxis_rotate=20)
    return bar_page.render_embed()


def usual_deal(spi, num_name, title):
    num_name_dict = {i.split(" ")[0]: i.split(" ")[1] for i in num_name}
    name_list = []
    value_list = []
    for num, value in spi:
        name_list.append(num_name_dict[num])
        value_list.append(value)

    return rank_bar(name_list, value_list, title)


# 购买数量排名
def usual_deal_amount_rank(request):
    """
    交易数量最多的，交易笔数最多的，交易总金额最多的
    :param request:
    :return:
    """
    choice_year = ""
    choice_name = ""

    date, num_name = choice_object()

    usual_amount = ProcurementInfo.objects.values_list("art_num", "amount")

    if request.method == "POST":
        choice_year = request.POST["year"]
        if choice_year:
            usual_amount = ProcurementInfo.objects.values_list("pro_date", "art_num", "amount")
            usual_amount = [[num, amo] for year, num, amo in usual_amount if str(year)[:4] == choice_year]

    amount = {}
    for num, amo in usual_amount:
        if num in amount:
            amount[num] += float(amo)
        else:
            amount[num] = float(amo)
    amount = sorted(amount.items(), key=lambda x: x[1], reverse=True)[:20]

    pattern = usual_deal(amount, num_name, "购入物品数量")

    context = dict(
        myechart=pattern,
        consumer=num_name,
        sell_date=date,
        date_year=choice_year,
        consumer_name=choice_name,
    )
    return render(request, "production/rank_year.html", context=context)


# 购买笔数排名
def usual_deal_adeal_rank(request):
    """
    交易数量最多的，交易笔数最多的，交易总金额最多的
    :param request:
    :return:
    """

    choice_year = ""
    choice_name = ""

    date, num_name = choice_object()

    usual_adeal = ProcurementInfo.objects.values_list("art_num", flat=True)

    if request.method == "POST":
        choice_year = request.POST["year"]
        if choice_year:
            usual_adeal = ProcurementInfo.objects.values_list("pro_date", "art_num")
            usual_adeal = [num for year, num in usual_adeal if str(year)[:4] == choice_year]

    adeal = Counter(usual_adeal).most_common(30)

    pattern = usual_deal(adeal, num_name, "购入物品笔数")

    context = dict(
        myechart=pattern,
        consumer=num_name,
        sell_date=date,
        date_year=choice_year,
        consumer_name=choice_name,
    )
    return render(request, "production/rank_year.html", context=context)


# 购买金额排名
def usual_deal_money_rank(request):
    """
    交易数量最多的，交易笔数最多的，交易总金额最多的
    :param request:
    :return:
    """
    choice_year = ""
    choice_name = ""

    date, num_name = choice_object()

    usual_money = ProcurementInfo.objects.values_list("art_num", "total_price")

    if request.method == "POST":
        choice_year = request.POST["year"]
        if choice_year:
            usual_money = ProcurementInfo.objects.values_list("pro_date", "art_num", "total_price")
            usual_money = [[num, tot] for year, num, tot in usual_money if str(year)[:4] == choice_year]

    money = {}
    for num, value in usual_money:
        if num in money:
            money[num] += float(value)
        else:
            money[num] = float(value)
    money = sorted(money.items(), key=lambda x: x[1], reverse=True)[:20]

    pattern = usual_deal(money, num_name, "购入物品金额")

    context = dict(
        myechart=pattern,
        consumer=num_name,
        sell_date=date,
        date_year=choice_year,
        consumer_name=choice_name,
    )
    return render(request, "production/rank_year.html", context=context)
