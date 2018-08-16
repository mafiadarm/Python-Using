from django.shortcuts import render, HttpResponse

# Create your views here.

from pyecharts import Bar3D, Pie
from .models import BalanceInfo, DepartmentInfo


# 柱状3D
def view_bar_3D(y_list, data_list, name=str()):
    """
    需要数据
    self.x_list 12个月的月份[日期] 等...
    self.y_list 各个不同的年份 等...
    self.date_list [[x, y, v], [x, y, v]] x和y是坐标索引，从0开始计算，v是展示的值
    :return:
    """
    x_list = ["{}月".format(i) for i in range(1, 13)]

    bar3d = Bar3D(name, width=1000, height=500)
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    print(x_list, y_list, data_list)
    bar3d.add("", x_list, y_list, data_list,
              is_visualmap=True,
              visual_range=[0, int(max(data_list, key=lambda x: x[2])[2])],
              visual_range_color=range_color,
              grid3d_width=200,
              grid3d_depth=80,
              is_toolbox_show=False,
              grid3d_shading='lambert',
              # is_grid3d_rotate=True,
              )

    return bar3d.render_embed()


# 首页
def index(request):
    spi = BalanceInfo.objects.filter(close_month__regex="[1][0-2]|[0][1-9]", bill_number__startswith="6001").values_list("close_year", "close_month",
                                                                               "domestic_currency_borrow")

    year_list = sorted({i[0] for i in spi})

    data_dict = {}
    for i in spi:
        y = i[0] + "-" + i[1]
        if y in data_dict:
            data_dict[y] += int(i[2])

        else:
            data_dict[y] = int(i[2])

    data_list = []
    for i, value in data_dict.items():
        year, month = i.split("-")
        data_list.append([int(month)-1, int(year)-int(min(year_list)), value])

    # print(data_dict)
    # return HttpResponse(data_dict)

    context = dict(
        myechart=view_bar_3D(year_list, data_list, "余额汇总表(月)"),
    )

    return render(request, "finance/index.html", context=context)


# 饼图
def pie(spi, name):
    """
    :param spi: 接受为可叠代对象,如:元组((),())
    :param name:
    :return:
    """
    attr = []
    v1 = []
    for i in spi:
        attr.append(i[0])
        v1.append(i[1])

    pie_pie = Pie("", title_pos='center', width=1200, height=600)
    pie_pie.add(name, attr, v1, radius=[25, 75], label_text_color=None,
                is_label_show=True, legend_orient='vertical', legend_pos='left', rosetype="area")
    return pie_pie.render_embed()


def depar_dict():
    dpi = DepartmentInfo.objects.all()
    dd = {i.depart_number:i.depart_name for i in dpi}
    return dd


def department(request):
    spi = BalanceInfo.objects.filter(
        close_month__regex="[1][0-2]|[0][1-9]",
        bill_number__startswith="6001"
    ).values_list(
        "department",
        "domestic_currency_borrow",
        "close_year",
        "close_month",
    )
    dpi = depar_dict()

    years = sorted({i[2] for i in spi})
    month = sorted({i[3] for i in spi})

    yy, cl = "", ""
    if request.method == "POST":
        yy = request.POST["year"]
        cl = request.POST["name"]

        if yy:
            spi = [i for i in spi if i[2] == str(yy)]

        if cl:
            spi = [i for i in spi if i[3] == str(cl)]

    pie_dict = {}
    for i in spi:
        if i[0] != "":
            d = dpi[i[0]]
        if d in pie_dict:
            pie_dict[d] += float(i[1])
        else:
            pie_dict[d] = float(i[1])

    context = dict(
        myechart=pie(sorted(pie_dict.items(), key=lambda x: x[1], reverse=True), "销售比例"),
        consumer=month,
        sell_date=years,
        date_year=yy,
        consumer_name=cl,
    )

    return render(request, "finance/rank.html", context=context)