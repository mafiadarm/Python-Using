from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar3D
from .models import SellProxyInfo


def index(request):
    if request.method == "POST":

        yy = request.POST["year"]

        return HttpResponse(yy)

    else:
        template = loader.get_template('sell/pyecharts.html')

        csm = SellProxyInfo.objects.all().values("consumer").distinct()
        consumer = [i.get("consumer") for i in csm]

        sd = SellProxyInfo.objects.all().values("sell_date")
        sell_date = sorted(list({str(i.get("sell_date"))[:4] for i in sd}))

        context = dict(
            myechart=view_bar_3D(),
            # title="直销数据汇总",
            consumer=consumer,
            sell_date=sell_date,
        )
        return HttpResponse(template.render(context, request))


def view_bar_3D():
    """
    需要数据
    self.x_list 12个月的月份[日期] 等...
    self.y_list 各个不同的年份 等...
    self.date_list [[x, y, v], [x, y, v]] x和y是坐标索引，从0开始计算，v是展示的值
    :return:
    """
    spi = SellProxyInfo.objects.all()

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

    data_list = [[int(k[5:7]) - 1, 2018 - int(k[:4]), int(v)] for k, v in value_dict.items()]

    y_list = sorted(list(y_set))
    x_list = ["{}月".format(i) for i in range(1, 13)]

    bar3d = Bar3D("直销销货汇总表", width=1000, height=500)
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

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
