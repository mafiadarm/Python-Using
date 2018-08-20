import datetime
import re
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from pyecharts import Bar3D, Bar, Pie, Map
from .models import SellProxyInfo, SellDirectInfo
from user_login import user_decorator
from pypinyin import lazy_pinyin


# 柱状3D
def view_bar_3D(spi, name=str()):
    """
    需要数据
    self.x_list 12个月的月份[日期] 等...
    self.y_list 各个不同的年份 等...
    self.date_list [[x, y, v], [x, y, v]] x和y是坐标索引，从0开始计算，v是展示的值
    :return:
    """
    y_set = set()
    value_dict = {}

    for i in spi:
        year = str(i.sell_date)[:4]
        ym = str(i.sell_date)[:7]

        y_set.add(year)

        if ym in value_dict:
            value_dict[ym] += int(i.total_price)
        else:
            value_dict[ym] = int(i.total_price)

    data_list = [[int(k[5:7]) - 1, int(k[:4]) - 2015, int(v)] for k, v in value_dict.items()]

    y_list = sorted(list(y_set))
    x_list = ["{}月".format(i) for i in range(1, 13)]

    bar3d = Bar3D(name + "销货汇总", width=1000, height=500)
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


# 首页
@user_decorator.login
def index(request):
    spi_s = SellProxyInfo.objects.all()
    spi_d = SellDirectInfo.objects.all()
    template = loader.get_template('sell/index.html')
    spi = []
    spi.extend(spi_s)
    spi.extend(spi_d)

    context = dict(
        myechart=view_bar_3D(spi),
    )

    return HttpResponse(template.render(context, request))


# 代理首页
@user_decorator.login
def proxy_index(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/index_proxy.html')
    context = dict(
        myechart=view_bar_3D(spi, "代理"),
    )

    return HttpResponse(template.render(context, request))


# 直营首页
@user_decorator.login
def direct_index(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/index_direct.html')

    context = dict(
        myechart=view_bar_3D(spi, "直销"),
    )

    return HttpResponse(template.render(context, request))


# 柱状图
def bar(name_list, value_list):
    bar_page = Bar("Ranking")
    bar_page.add("排名", name_list, value_list, xaxis_rotate=20)
    return bar_page.render_embed()


# 代理商 排名
@user_decorator.login
def proxy_ranking(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.proxy: lazy_pinyin(i.proxy) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""

    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.proxy == cl]

    count = {}
    for i in spi:
        if i.proxy in count:
            count[i.proxy] += int(i.total_price)
        else:
            count[i.proxy] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    name_list = []
    value_list = []
    for name, value in splite_list:
        name_list.append(name)
        value_list.append(value)

    context = dict(
        myechart=bar(name_list, value_list),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 代理商 客户排名
@user_decorator.login
def proxy_client_ranking(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.company: lazy_pinyin(i.company) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""

    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.company == cl]

    count = {}
    for i in spi:
        if i.company in count:
            count[i.company] += int(i.total_price)
        else:
            count[i.company] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    name_list = []
    value_list = []
    for name, value in splite_list:
        name_list.append(name)
        value_list.append(value)

    context = dict(
        myechart=bar(name_list, value_list),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 直营 排名
@user_decorator.login
def direct_ranking(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.consumer: lazy_pinyin(i.consumer) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""

    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.consumer == cl]

    count = {}
    for i in spi:
        if i.consumer in count:
            count[i.consumer] += int(i.total_price)
        else:
            count[i.consumer] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    name_list = []
    value_list = []
    for name, value in splite_list:
        name_list.append(name)
        value_list.append(value)

    context = dict(
        myechart=bar(name_list, value_list),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 直营 销售员 排名
@user_decorator.login
def direct_staff_ranking(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.staff: lazy_pinyin(i.staff) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""

    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.staff == cl]

    count = {}
    for i in spi:
        if i.staff in count:
            count[i.staff] += int(i.total_price)
            # if i.staff == "王彬":
            #     print(i.sell_date, i.consumer, i.article, i.staff, i.total_price)
        else:
            count[i.staff] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    name_list = []
    value_list = []
    for name, value in splite_list:
        name_list.append(name)
        value_list.append(value)

    context = dict(
        myechart=bar(name_list, value_list),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 直营 部门 排名
@user_decorator.login
def direct_depart_ranking(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.department: lazy_pinyin(i.department) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""

    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.department == cl]

    count = {}
    for i in spi:
        if i.department in count:
            count[i.department] += int(i.total_price)
        else:
            count[i.department] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    name_list = []
    value_list = []
    for name, value in splite_list:
        name_list.append(name)
        value_list.append(value)

    context = dict(
        myechart=bar(name_list, value_list),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 产品总排名
@user_decorator.login
def product_ranking(request):
    spi_p = SellProxyInfo.objects.all()
    spi_d = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')
    spi = []
    spi.extend(spi_p)
    spi.extend(spi_d)

    article = {i.article: lazy_pinyin(i.article) for i in spi}  #
    article = sorted(article.items(), key=lambda x: x[1])
    article = [i[0] for i in article]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""

    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.article == cl]  #

    count = {}
    for i in spi:
        if i.article in count:  #
            count[i.article] += int(i.total_price)  #
        else:
            count[i.article] = int(i.total_price)  #

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    name_list = []
    value_list = []
    for name, value in splite_list:
        name_list.append(name)
        value_list.append(value)

    context = dict(
        myechart=bar(name_list, value_list),
        consumer=article,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


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
        day_list.append(str(start_date))
        start_date += day_plus

    value_list = [0] * len(day_list)
    for i in spi:
        flag = value_list[day_list.index(str(i.sell_date))]
        if flag:
            value_list[day_list.index(str(i.sell_date))] += int(i.total_price)
        else:
            value_list[day_list.index(str(i.sell_date))] = int(i.total_price)
    # print(value_list)
    barzoom = Bar()
    barzoom.add(name + " " + year + " 交易概况", day_list, value_list,
                is_datazoom_show=True, datazoom_type="both", xaxis_rotate=0, datazoom_range=[0, 100])
    return barzoom.render_embed()


# 代理商 下单记录
@user_decorator.login
def proxy_customer_record(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.proxy: lazy_pinyin(i.proxy) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.proxy == cl]

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer,
        sell_date=sell_date,
        date_year="",
        consumer_name="",
    )
    return HttpResponse(template.render(context, request))


# 代理商 客户下单记录
@user_decorator.login
def proxy_client_customer_record(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.company: lazy_pinyin(i.company) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.company == cl]

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer,
        sell_date=sell_date,
        date_year="",
        consumer_name="",
    )
    return HttpResponse(template.render(context, request))


# 直营 客户下单记录
@user_decorator.login
def direct_customer_record(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.consumer: lazy_pinyin(i.consumer) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.consumer == cl]

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 直营 销售员下单记录
@user_decorator.login
def direct_staff_record(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.staff: lazy_pinyin(i.staff) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if cl:
            spi = [i for i in spi if i.staff == cl]
        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer,
        sell_date=sell_date,
        date_year="",
        consumer_name="",
    )
    return HttpResponse(template.render(context, request))


# 直营 部门下单记录
@user_decorator.login
def direct_depart_record(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    consumer = {i.department: lazy_pinyin(i.department) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.department == cl]

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer,
        sell_date=sell_date,
        date_year="",
        consumer_name="",
    )
    return HttpResponse(template.render(context, request))


# 产品销售记录
@user_decorator.login
def product_record(request):
    spi_p = SellProxyInfo.objects.all()
    spi_d = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')
    spi = []
    spi.extend(spi_p)
    spi.extend(spi_d)

    consumer = {i.article: lazy_pinyin(i.article) for i in spi}
    consumer = sorted(consumer.items(), key=lambda x: x[1])
    consumer = [i[0] for i in consumer]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.article == cl]

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 代理商 下单记录 前10
@user_decorator.login
def proxy_customer_record_ten(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.proxy == cl]

    count = {}
    for i in spi:
        if i.proxy in count:
            count[i.proxy] += int(i.total_price)
        else:
            count[i.proxy] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    consumer_ten = [name for name, _ in splite_list]

    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer_ten,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 代理 客户下单记录 前10
@user_decorator.login
def proxy_client_customer_record_ten(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.company == cl]

    count = {}
    for i in spi:
        if i.company in count:
            count[i.company] += int(i.total_price)
        else:
            count[i.company] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = splite_list[:10]
    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)

    consumer_ten = [name for name, _ in splite_list]

    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer_ten,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 直营 客户下单记录 前10
@user_decorator.login
def direct_customer_record_ten(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.consumer == cl]

    count = {}
    for i in spi:
        if i.consumer in count:
            count[i.consumer] += int(i.total_price)
        else:
            count[i.consumer] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = splite_list[:10]
    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)

    consumer_ten = [name for name, _ in splite_list]

    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer_ten,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 销售员 下单记录 前10
@user_decorator.login
def direct_staff_record_ten(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi = [i for i in spi if i.staff == cl]

    count = {}
    for i in spi:
        if i.staff in count:
            count[i.staff] += int(i.total_price)
        else:
            count[i.staff] = int(i.total_price)

    splite_list = []
    for k, v in count.items():
        splite_list.append([k, v])

    splite_list = sorted(splite_list, key=lambda x: x[1], reverse=True)
    splite_list = splite_list[:10]

    consumer_ten = [name for name, _ in splite_list]

    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    context = dict(
        myechart=datazoom(spi, yy, cl),
        consumer=consumer_ten,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )
    return HttpResponse(template.render(context, request))


# 饼图
def pie(spi, name):
    """
    :param spi: 接受为元组((),())
    :param name:
    :return:
    """
    attr = []
    v1 = []
    for i in spi:
        attr.append(i[0])
        v1.append(i[1])

    pie_pie = Pie(name, title_pos='center')
    pie_pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
                is_label_show=True, legend_orient='vertical', legend_pos='left')
    return pie_pie.render_embed()


# 产品汇总饼图 区分 水剂 粉剂 设备
@user_decorator.login
def product_ratio(request):
    """
    需要增加品号
    """
    spi_s = SellProxyInfo.objects.all()
    spi_d = SellDirectInfo.objects.all()
    template = loader.get_template('sell/index_product.html')
    spi = []
    spi.extend(spi_s)
    spi.extend(spi_d)

    wp_dict = {
        "water": 0,
        "powder": 0,
        "machine": 0,
    }
    regx_wp = re.compile("102\d{9}|103\d{9}]")
    regx_ma = re.compile("110\d{8}")

    for i in spi:
        if regx_wp.findall(str(i.art_num)):
            if "ml" in i.unit:
                wp_dict["water"] += int(i.total_price)
            elif "kg" in i.unit:
                wp_dict["powder"] += int(i.total_price)
        elif regx_ma.findall(str(i.art_num)):
            wp_dict["machine"] += int(i.total_price)

    context = dict(
        myechart=pie(wp_dict.items(), "三类产品总占比"),
    )

    return HttpResponse(template.render(context, request))


# 直销产品汇总饼图 区分 水剂 粉剂 设备
@user_decorator.login
def product_ratio_direct(request):
    spi = SellDirectInfo.objects.all()
    template = loader.get_template('sell/index_product.html')

    wp_dict = {
        "water": 0,
        "powder": 0,
        "machine": 0,
    }
    regx_wp = re.compile("102\d{9}|103\d{9}]")
    regx_ma = re.compile("110\d{8}")

    for i in spi:
        if regx_wp.findall(str(i.art_num)):
            if "ml" in i.unit:
                wp_dict["water"] += int(i.total_price)
            elif "kg" in i.unit:
                wp_dict["powder"] += int(i.total_price)
        elif regx_ma.findall(str(i.art_num)):
            wp_dict["machine"] += int(i.total_price)

    context = dict(
        myechart=pie(wp_dict.items(), "直销产品占比"),
    )

    return HttpResponse(template.render(context, request))


# 代理产品汇总饼图 区分 水剂 粉剂 设备
@user_decorator.login
def product_ratio_proxy(request):
    spi = SellProxyInfo.objects.all()
    template = loader.get_template('sell/index_product.html')

    wp_dict = {
        "water": 0,
        "powder": 0,
        "machine": 0,
    }
    regx_wp = re.compile("102\d{9}|103\d{9}]")
    regx_ma = re.compile("110\d{8}")

    for i in spi:
        if regx_wp.findall(str(i.art_num)):
            if "ml" in i.unit:
                wp_dict["water"] += int(i.total_price)
            elif "kg" in i.unit:
                wp_dict["powder"] += int(i.total_price)
        elif regx_ma.findall(str(i.art_num)):
            wp_dict["machine"] += int(i.total_price)

    context = dict(
        myechart=pie(wp_dict.items(), "代理产品占比"),
    )

    return HttpResponse(template.render(context, request))


# 柱状堆叠图  for def product_pile
def bar_pile(spi, name):
    # spi = {"品名": {"直销": "价格", "代理": "价格"}, "品名": {"直销": "价格", "代理": "价格"}}
    attr = []
    v1 = []
    v2 = []
    for k, v in spi.items():
        attr.append(k)
        v1.append(v["直营"])
        v2.append(v["代理"])

    bar_p = Bar(name)
    bar_p.add("直营", attr, v1, is_stack=True)
    bar_p.add("代理", attr, v2, is_stack=True, xaxis_rotate=20)
    return bar_p.render_embed()


# 产品堆叠图 分直销和代理 没区分产品
@user_decorator.login
def product_pile(request):
    spi_p = SellProxyInfo.objects.all()
    spi_d = SellDirectInfo.objects.all()
    template = loader.get_template('sell/rank.html')
    spi = []
    spi.extend(spi_p)
    spi.extend(spi_d)

    article = {i.article: lazy_pinyin(i.article) for i in spi}  #
    article = sorted(article.items(), key=lambda x: x[1])
    article = [i[0] for i in article]
    sell_date = sorted(list({str(i.sell_date)[:4] for i in spi}))

    yy = ""
    cl = ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if str(i.sell_date)[:4] == str(yy)]
        if cl:
            spi_p = [i for i in spi if i.article == cl]  #
            spi_d = [i for i in spi if i.article == cl]  #

    # 统计产品在代理商和直营分别总和
    count = {}
    for i in spi_p:
        if i.article in count:
            count[i.article]["代理"] += int(i.total_price)
        else:
            count[i.article] = {"代理": int(i.total_price), "直营": 0}

    for i in spi_d:
        if i.article in count:
            count[i.article]["直营"] += int(i.total_price)
        else:
            count[i.article] = {"直营": int(i.total_price), "代理": 0}

    count_all = {k: sum(v.values()) for k, v in count.items()}
    count_10 = sorted(count_all.items(), key=lambda x: x[1], reverse=True)[:20]
    # print(count_10)
    count_dict = OrderedDict({i[0]: count[i[0]] for i in count_10})

    context = dict(
        myechart=bar_pile(count_dict, "产品堆叠图（前10）"),
        consumer=article,
        sell_date=sell_date,
        date_year=yy,
        consumer_name=cl,
    )

    return HttpResponse(template.render(context, request))
