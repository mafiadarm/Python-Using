#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_08_2018  11:04
    File Name:      /GitHub/data_view
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    http://blog.csdn.net/youzhouliu/article/details/78361503
    drawing use Plotly
==============================
"""

import logging
import random

import math
from pyecharts import Bar
from pyecharts import EffectScatter
from pyecharts import Funnel
from pyecharts import Gauge
from pyecharts import Geo
from pyecharts import Graph
from pyecharts import Line
from pyecharts import Liquid
from pyecharts import Map
from pyecharts import Parallel
from pyecharts import Pie
from pyecharts import Polar
from pyecharts import Radar
from pyecharts import Scatter
from pyecharts import WordCloud

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

def singeObjectView(title, subhead, icon_name, obj_name=list, obj_data=list):
    """
    单项目柱状图
    :param title: 主题
    :param subhead: 副主题
    :param icon_name: 图标名称
    :param obj_name: 项目名称
    :param obj_data: 项目名称对应的项目值
    :return: 生成render.html 在当前目录
    """
    bar = Bar(title, subhead)
    bar.add(icon_name, obj_name, obj_data)
    bar.show_config()
    bar.render()

def barChart():
    """
    chart1 柱状图/chart2 条形图
    :return:
    """
    attr = ["obj1", "obj2", "obj3", "obj4", "obj5"]
    v1 = [14, 26, 22, 30, 7]
    v2 = [4, 33, 20, 25, 18]

    bar = Bar("标记线和标记点示例")
    bar.add("商家A", attr, v1, mark_point=["average"])
    bar.add("商家B", attr, v2, mark_line=["min", "max"])
    bar.render(path="C:/Users\lo\Desktop\html/bar_chart1.html")

    bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", attr, v1)
    bar.add("商家B", attr, v2, is_convert=True)
    bar.render(path="C:/Users\lo\Desktop\html/bar_chart2.html")

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    bar = Bar("柱状图示例")
    bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    bar.show_config()
    bar.render(path="C:/Users\lo\Desktop\html/bar_chart3.html")

def effectScatter():
    """
    带有涟漪特效动画的散点图
    :return:
    """
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [25, 20, 15, 10, 60, 33]
    es = EffectScatter("动态散点图示例")
    es.add("effectScatter", v1, v2)
    es.render(path="C:/Users\lo\Desktop\html/effectScatter1.html")

    es = EffectScatter("动态散点图各种图形示例")
    es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
    es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4, symbol="rect")
    es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5, symbol="roundRect")
    es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill', symbol="diamond")
    es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3, symbol="arrow")
    es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3, symbol="triangle")
    es.render(path="C:/Users\lo\Desktop\html/effectScatter2.html")

def funnelMap():
    """
    漏斗图
    :return:
    """
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    funn = Funnel("漏斗图示例")
    funn.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
    funn.render(path="C:/Users\lo\Desktop\html/funnel.html")

def wheelGauge():
    """
    仪表盘
    :return:
    """
    gauge = Gauge("仪表盘示例")
    gauge.add("业务指标", "完成率", 42.66)
    # gauge.show_config()
    gauge.render(path="C:/Users\lo\Desktop\html/gauge.html")

def geographyHotPoint():
    """
    地图热点
    Here is a list of map extensions from pyecharts dev team:
    1.World countries include China map and World map: echarts-countries-pypkg (1.9MB)
    2.Chinese provinces and regions: echarts-china-provinces-pypkg (730KB)
    3.Chinese cities: echarts-china-cities-pypkg (3.8MB)

    In order to install them, you can try one of them or all:
    $ pip install echarts-countries-pypkg
    $ pip install echarts-china-provinces-pypkg
    $ pip install echarts-china-cities-pypkg
    :return:
    """
    data = [('三亚市', '10'), ('海口市', '13'), ('汕尾市', '15'), ('汕头市', '15'), ('三明市', '15'), ('惠州市', '15'), ('东莞市', '15'), ('潮州市', '15'), ('二连浩特市', '16'), ('揭阳市', '16'), ('中山市', '16'), ('河源市', '17'), ('深圳市', '18'), ('衢州市', '18'), ('江门市', '18'), ('广州市', '18'), ('香格里拉', '19'), ('肇庆市', '19'), ('南平市', '19'), ('阳江市', '20'), ('龙岩市', '20'), ('北海市', '21'), ('湛江市', '22'), ('梅州市', '22'), ('黄山市', '22'), ('佛山市', '22'), ('巢湖市', '22'), ('漳州市', '23'), ('云浮市', '23'), ('厦门市', '23'), ('泉州市', '23'), ('莆田市', '23'), ('南宁市', '23'), ('韶关市', '24'), ('茂名市', '25'), ('丽水市', '25'), ('阿里', '25'), ('香港特别行政区', '25'), ('温州市', '26'), ('柳州市', '26'), ('福州市', '26'), ('那曲', '26'), ('兴安盟', '27'), ('珠海市', '27'), ('鹰潭市', '27'), ('台州市', '27'), ('南昌市', '27'), ('上饶市', '28'), ('九江市', '28'), ('金华市', '28'), ('诸暨市', '29'), ('义乌市', '29'), ('通辽市', '29'), ('呼伦贝尔市', '29'), ('盘锦市', '29'), ('朝阳市', '29'), ('重庆市', '29'), ('承德市', '30'), ('忻州市', '30'), ('锦州市', '30'), ('阜新市', '30'), ('景德镇市', '30'), ('抚州市', '30'), ('瓦房店市', '31'), ('临安市', '32'), ('莱州市', '32'), ('丹东市', '32'), ('宜春市', '32'), ('绍兴市', '32'), ('萍乡市', '32'), ('日喀则', '32'), ('泸州市', '32'), ('甘孜', '32'), ('张家口市', '33'), ('秦皇岛市', '33'), ('赤峰市', '33'), ('葫芦岛市', '33'), ('杭州市', '33'), ('滨州市', '33'), ('昌都', '33'), ('桂林市', '34'), ('东营市', '34'), ('拉萨市', '34'), ('迪庆', '34'), ('寿光市', '35'), ('株洲市', '35'), ('衡阳市', '35'), ('常德市', '35'), ('内江市', '35'), ('林芝', '35'), ('阿坝', '35'), ('乳山市', '36'), ('阿拉善盟', '36'), ('遵义市', '36'), ('昭通市', '36'), ('山南', '36'), ('曲靖市', '36'), ('荣成市', '37'), ('呼和浩特市', '37'), ('铁岭市', '37'), ('大庆市', '37'), ('大连市', '37'), ('舟山市', '37'), ('永州市', '37'), ('长沙市', '37'), ('安庆市', '37'), ('克拉玛依市', '37'), ('巴中市', '37'), ('鄂尔多斯市', '38'), ('娄底市', '38'), ('吉安市', '38'), ('文山', '38'), ('乐山市', '38'), ('齐齐哈尔市', '39'), ('牡丹江市', '39'), ('吉林市', '39'), ('攀枝花市', '39'), ('沈阳市', '40'), ('湘潭市', '40'), ('宁波市', '40'), ('赣州市', '40'), ('恩施', '40'), ('沧州市', '41'), ('营口市', '41'), ('益阳市', '41'), ('遂宁市', '41'), ('胶州市', '42'), ('平度市', '42'), ('新余市', '42'), ('铜陵市', '42'), ('六安市', '42'), ('宜宾市', '42'), ('怒江傈', '42'), ('丽江市', '42'), ('广元市', '42'), ('即墨市', '43'), ('蓬莱市', '43'), ('招远市', '43'), ('邵阳市', '43'), ('眉山市', '43'), ('富阳市', '44'), ('文登市', '44'), ('黄冈市', '44'), ('哈尔滨市', '45'), ('潍坊市', '45'), ('泰安市', '45'), ('达州市', '45'), ('淄博市', '46'), ('烟台市', '46'), ('雅安市', '46'), ('包头市', '47'), ('黄石市', '47'), ('玉溪市', '47'), ('大理', '47'), ('保山市', '47'), ('莱西市', '48'), ('朔州市', '48'), ('张家界市', '49'), ('神农架', '50'), ('威海市', '50'), ('德州市', '50'), ('自贡市', '50'), ('红河哈尼族', '50'), ('成都市', '50'), ('章丘市', '51'), ('天津市', '51'), ('辽阳市', '51'), ('芜湖市', '51'), ('鄂州市', '51'), ('临沧市', '51'), ('晋中市', '52'), ('南充市', '52'), ('嘉峪关市', '52'), ('胶南市', '53'), ('咸宁市', '53'), ('十堰市', '53'), ('延安市', '53'), ('昆明市', '53'), ('吕梁市', '54'), ('鞍山市', '54'), ('岳阳市', '54'), ('青岛市', '54'), ('济宁市', '54'), ('郴州市', '54'), ('凉山', '54'), ('广安市', '54'), ('衡水市', '55'), ('锡林郭勒盟', '55'), ('宣城市', '55'), ('贵阳市', '55'), ('长春市', '56'), ('池州市', '56'), ('德宏', '56'), ('廊坊市', '57'), ('日照市', '57'), ('合肥市', '57'), ('楚雄', '57'), ('资阳市', '57'), ('抚顺市', '58'), ('本溪市', '58'), ('济南市', '58'), ('乌海市', '59'), ('大同市', '59'), ('莱芜市', '59'), ('金昌市', '59'), ('临汾市', '60'), ('临沂市', '60'), ('连云港市', '61'), ('嘉兴市', '61'), ('聊城市', '62'), ('德阳市', '63'), ('唐山市', '65'), ('湖州市', '65'), ('乌鲁木齐市', '65'), ('石嘴山市', '65'), ('银川市', '66'), ('菏泽市', '67'), ('北京市', '68'), ('荆州市', '68'), ('太原市', '69'), ('随州市', '69'), ('武汉市', '70'), ('铜川市', '70'), ('巴彦淖尔市', '71'), ('商丘市', '71'), ('清远市', '71'), ('鹤壁市', '71'), ('上海市', '72'), ('孝感市', '72'), ('绵阳市', '72'), ('咸阳市', '73'), ('宜昌市', '74'), ('济源', '75'), ('濮阳市', '75'), ('淮南市', '75'), ('亳州市', '75'), ('仙桃', '79'), ('渭南市', '80'), ('西安市', '81'), ('邢台市', '82'), ('荆门市', '82'), ('溧阳市', '83'), ('宜兴市', '84'), ('淮北市', '84'), ('西双版纳', '84'), ('吴江市', '86'), ('运城市', '86'), ('郑州市', '87'), ('焦作市', '87'), ('阜阳市', '87'), ('信阳市', '89'), ('滁州市', '89'), ('澳门', '91'), ('阳泉市', '92'), ('长治市', '92'), ('开封市', '92'), ('马鞍山市', '93'), ('潜江', '94'), ('邯郸市', '94'), ('保定市', '94'), ('洛阳市', '96'), ('枣庄市', '97'), ('许昌市', '98'), ('昆山市', '99'), ('盐城市', '99'), ('西宁市', '100'), ('无锡市', '101'), ('石家庄市', '102'), ('宝鸡市', '102'), ('兰州市', '103'), ('蚌埠市', '106'), ('安阳市', '107'), ('南京市', '109'), ('苏州市', '110'), ('周口市', '110'), ('海门市', '114'), ('淮安市', '122'), ('宿州市', '126'), ('句容市', '127'), ('驻马店市', '128'), ('三门峡市', '129'), ('徐州市', '130'), ('太仓市', '132'), ('南通市', '134'), ('平顶山市', '138'), ('宿迁市', '139'), ('金坛市', '141'), ('江阴市', '150'), ('常州市', '153'), ('常熟市', '156'), ('泰州市', '160'), ('张家港市', '171'), ('扬州市', '175'), ('漯河市', '175'), ('晋城市', '177'), ('南阳市', '181'), ('襄阳市', '191'), ('镇江市', '192'), ('库尔勒', '415')]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
    geo.show_config()
    geo.render(path="C:/Users\lo\Desktop\html/geographyHotPoint1.html")

    data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
    geo.show_config()
    geo.render(path="C:/Users\lo\Desktop\html/geographyHotPoint2.html")

def relateGraph():
    """
    关系图
    :return:
    """
    nodes = [{"name": "结点1", "symbolSize": 8}, {"name": "结点2", "symbolSize": 4}, {"name": "结点3", "symbolSize": 2},
             {"name": "结点4", "symbolSize": 4}, {"name": "结点5", "symbolSize": 5}, {"name": "结点6", "symbolSize": 4},
             {"name": "结点7", "symbolSize": 3}, {"name": "结点8", "symbolSize": 2}]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    graph = Graph("关系图-环形布局示例")
    graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
    # graph.show_config()
    graph.render(path="C:/Users\lo\Desktop\html/Graph.html")

    # with open("..jsonweibo.json", "r", encoding="utf-8") as f:
    #     j = json.load(f)
    #     nodes, links, categories, cont, mid, userl = j
    # graph = Graph("微博转发关系图", width=1200, height=600)
    # graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False, line_curve=0.2, label_text_color=None)
    # # graph.show_config()
    # graph.render(path="C:/Users\lo\Desktop\html/Graph_weibo.html")

def brokenLine():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    line = Line("折线图示例")
    line.add("商家A", attr, v1, mark_point=["average"])
    line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine1.html")

    line = Line("折线图-阶梯图示例")
    line.add("商家A", attr, v1, is_step=True, is_label_show=True)
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine2.htm")

    line = Line("折线图-面积图示例")
    line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
    line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine3.htm")

    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
    line = Line("折线图示例")
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], yaxis_formatter="°C")
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine4.htm")

def waterBall():
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    liquid.show_config()
    liquid.render(path="C:/Users\lo\Desktop\html/liquid1.htm")

    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    liquid.show_config()
    liquid.render(path="C:/Users\lo\Desktop\html/liquid2.htm")

    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
    liquid.show_config()
    liquid.render(path="C:/Users\lo\Desktop\html/liquid3.htm")

def mapHotPoint():
    """
    地图块显示
    Map 结合 VisualMap 示例
    :return: 
    """
    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    mapp = Map("全国地图示例", width=1200, height=600)
    mapp.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
    mapp.show_config()
    mapp.render(path="C:/Users\lo\Desktop\html/mapHotPoint1.htm")

    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    mapp = Map("广东地图示例", width=1200, height=600)
    mapp.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
    mapp.show_config()
    mapp.render(path="C:/Users\lo\Desktop\html/mapHotPoint2.htm")

def parallelCoordinates():
    """
    平行坐标系
    :return:
    """
    c_schema = [{"dim": 0, "name": "data"}, {"dim": 1, "name": "AQI"}, {"dim": 2, "name": "PM2.5"},
                {"dim": 3, "name": "PM10"}, {"dim": 4, "name": "CO"}, {"dim": 5, "name": "NO2"},
                {"dim": 6, "name": "CO2"},
                {"dim": 7, "name": "等级", "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}]
    data = [[1, 91, 45, 125, 0.82, 34, 23, "良"], [2, 65, 27, 78, 0.86, 45, 29, "良"], [3, 83, 60, 84, 1.09, 73, 27, "良"],
            [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
            [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
            [8, 89, 65, 78, 0.86, 51, 26, "良"], [9, 53, 33, 47, 0.64, 50, 17, "良"], [10, 80, 55, 80, 1.01, 75, 24, "良"],
            [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"], [12, 99, 71, 142, 1.1, 62, 42, "良"],
            [13, 95, 69, 130, 1.28, 74, 50, "良"], [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]]
    parallel = Parallel("平行坐标系-用户自定义指示器")
    parallel.config(c_schema=c_schema)
    parallel.add("parallel", data)
    parallel.show_config()
    parallel.render(path="C:/Users\lo\Desktop\html/parallel.htm")

def cookiePie():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例")
    pie.add("", attr, v1, is_label_show=True)
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie1.htm")

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    v2 = [19, 21, 32, 20, 20, 33]
    pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
    pie.add("商品A", attr, v1, center=[15, 50], is_random=True, radius=[30, 75], rosetype='radius')
    pie.add("商品B", attr, v2, center=[65, 50], is_random=True, radius=[30, 75], rosetype='area', is_legend_show=False, is_label_show=True)
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie2.htm")

    pie = Pie("饼图嵌套示例", title_pos='center', width=1000, height=600)
    pie.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148], radius=[40, 55], is_label_show=True)
    pie.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30], legend_orient='vertical', legend_pos='left')
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie3.htm")

    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    pie = Pie("饼图示例", width=1000, height=600)
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[25, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[25, 50], rosetype='area')
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[65, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[65, 50], rosetype='radius')
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie4.htm")

    pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
    pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
    pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie5.htm")

def polarCoordinates():
    """
    极坐标系
    :return:
    """
    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
    polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
    polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
    polar.show_config()
    polar.render(path="C:/Users\lo\Desktop\html/polar1.htm")

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
    polar.show_config()
    polar.render(path="C:/Users\lo\Desktop\html/polar2.htm")

    data = []
    for i in range(5):
        for j in range(101):
            theta = j / 100 * 360
            alpha = i * 360 + theta
            r = math.pow(math.e, 0.003 * alpha)
            data.append([r, theta])
    polar = Polar("极坐标系示例")
    polar.add("", data, symbol_size=0, symbol='circle', start_angle=-25, is_radiusaxis_show=False, area_color="#f3c5b3", area_opacity=0.5, is_angleaxis_show=False)
    polar.show_config()
    polar.render(path="C:/Users\lo\Desktop\html/polar3.htm")


def radarCycle():
    schema = [("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar()
    radar.config(schema)
    radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
    radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
    radar.show_config()
    radar.render(path="C:/Users\lo\Desktop\html/radar1.htm")

    value_bj = [[55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2], [56, 7, 63, 0.3, 14, 5, 3],
                [33, 7, 29, 0.33, 16, 6, 4]]
    value_sh = [[91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2], [83, 60, 84, 1.09, 73, 27, 3],
                [109, 81, 121, 1.28, 68, 51, 4]]
    c_schema = [{"name": "AQI", "max": 300, "min": 5}, {"name": "PM2.5", "max": 250, "min": 20},
                {"name": "PM10", "max": 300, "min": 5}, {"name": "CO", "max": 5}, {"name": "NO2", "max": 200},
                {"name": "SO2", "max": 100}]
    radar = Radar()
    radar.config(c_schema=c_schema, shape='circle')
    radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
    radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
    radar.show_config()
    radar.render(path="C:/Users\lo\Desktop\html/radar2.htm")

def scatterPoint():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    scatter.show_config()
    scatter.render(path="C:/Users\lo\Desktop\html/scatter1.htm")

    # scatter = Scatter("散点图示例")
    # v1, v2 = scatter.draw("../images/pyecharts-0.png")
    # scatter.add("pyecharts", v1, v2, is_random=True)
    # scatter.show_config()
    # scatter.render(path="C:/Users\lo\Desktop\html/scatter2.htm")

def wordCloud():
    name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A',
            'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton',
            'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament',
            'Point Break']
    value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273,
             265]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render(path="C:/Users\lo\Desktop\html/wordCloud1.htm")

    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
    wordcloud.show_config()
    wordcloud.render(path="C:/Users\lo\Desktop\html/wordCloud2.htm")

if __name__ == '__main__':
    barChart()
    effectScatter()
    funnelMap()
    wheelGauge()
    geographyHotPoint()
    relateGraph()
    brokenLine()
    waterBall()
    mapHotPoint()
    parallelCoordinates()
    cookiePie()
    polarCoordinates()
    radarCycle()
    scatterPoint()
    wordCloud()