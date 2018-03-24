#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_20_2018  11:29
    File Name:      /pychart_SqlServer/views
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    视图模板，继承数据清洗和预置信息
==============================
"""
__author__ = 'Loffew'

import datetime
import random
import math
from make_data import *
from connection import *
from random import randint
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
from pyecharts import Page
from pyecharts import Bar3D
from pyecharts import HeatMap
from pyecharts import Kline
from pyecharts import Line3D
from pyecharts import Sankey
from pyecharts import Scatter3D
from pyecharts import ThemeRiver
from pyecharts import Grid  # 组合图
from pyecharts import Overlap
from pyecharts import Timeline

# BASE_path = os.getcwd()


class Views(MakeData, ConnectPackage):
    def __init__(self):
        """
        通用的设置
        self.start_year str() 用于显示在网页和html文件名上
        self.title_name str() 用于显示在web标签页上，默认为Echats
        self.table_name str() 放在网页上展示的名字
        self.html_name 用于保存html文件名上的名字
        """
        super(Views, self).__init__()
        super(MakeData, self).__init__()
        super(ConnectPackage, self).__init__()

        self.BASE_PATH = ""

    def view_date_hot(self):
        """
        需要的数据
        self.start_year str() 用于显示在网页和html文件名上
        self.data_dict 展示的数据：
            [["year-month-day", value],["year-month-day", value],["year-month-day", value]]
        """
        print("开始生成 %s年 %s每日销货汇总热力图" % (self.start_year, self.table_name))

        heat_map = HeatMap("%s每日销货汇总热力图" % self.table_name, "%s年" % self.start_year, width=1200)
        heat_map.add("", self.data_dict, is_calendar_heatmap=True, visual_text_color='#000', visual_range_text=['', ''],
                     visual_range=[0, max(self.data_dict, key=lambda x:x[1])], calendar_cell_size=['auto', 30],
                     is_visualmap=True, calendar_date_range=str(self.start_year), visual_pos="5%",
                     visual_top="75%", visual_orient='horizontal', is_toolbox_show=False)
        heat_map.render(path=self.BASE_PATH + "{}{}_data_hot.html".format(self.start_year, self.html_name))

    def view_block_area_map(self):
        """
        需要的数据
        self.data_list
            [(province, value), (province, value)]
        :return:
        """
        print("开始生成 %s年 全国%s 销货汇总热力图" % (self.start_year, self.table_name))
        c_map = Map("全国%s 销货汇总热力图" % self.table_name, "%s年" % self.start_year, width=1200, height=600)
        pro = [province for province, _ in self.data_list]
        val = [value for _, value in self.data_list]

        c_map.add("", pro, val, maptype='china', is_visualmap=True, visual_range=[min(val), max(val)],
                  visual_text_color="#fff", symbol_size=15, is_toolbox_show=False)
        c_map.render(path=self.BASE_PATH + "{}{}_sales_hot_area.html".format(self.start_year, self.html_name))

    def view_bar_3D(self):
        """
        需要数据
        self.x_list 12个月的月份[日期] 等...
        self.y_list 各个不同的年份 等...
        self.date_list [[x, y, v], [x, y, v]] x和y是坐标索引，从0开始计算，v是展示的值
        :return:
        """
        bar3d = Bar3D("%s年度销货汇总总表" % self.table_name, width=1200, height=800)
        range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                       '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        bar3d.add("", self.x_list, self.y_list, [[d[0], d[1], d[2]] for d in self.date_list],
                  is_visualmap=True, visual_range=[0, max(self.data_list, key=lambda x: x[2])[2]],
                  visual_range_color=range_color, grid3d_width=200, grid3d_depth=80, is_toolbox_show=False)
        bar3d.render(path=self.BASE_PATH + "%s3D_display.html" % self.html_name)

    def view_growth_compare(self, score, **kwargs):
        """
        对比各条数据
        :param score: 刻度 [score]
        :param kwargs: {"name": [value],}
        """
        line = Line("销货曲线", width=1800, height=600, page_title="Sales line")
        for name, value in kwargs.items():
            line.add(name, score, value, is_smooth=True, mark_line=["max", "average"], is_toolbox_show=False,
                     label_emphasis_textcolor="#000")
        line.render(path=self.BASE_PATH + "compare_line.html")

    def view_data_of_pie(self):
        """
        饼图对比
        self.x_list 项目列表[object1， object2]
        self.date_list 对应项目列表的数据列表，一个项目对应一个数据[value1， value2]
        :return:
        """
        pie = Pie("%s占比图" % self.table_name, width=900)
        pie.add("", self.x_list, self.data_list, radius=[30, 75], is_random=True, label_text_color=None, is_label_show=True,
                legend_top="95%", is_toolbox_show=False)
        pie.render(path=self.BASE_PATH + "%s compare_line.html" % self.html_name)

    def view_bar_datazoom(self):
        """
        以日期为刻度，对比各条数据
        self.date_list: 刻度 [date]
        self.data_dicto_compare: {"name": [value],}
        """
        bar = Bar("日销货一览", width=1800, height=600, page_title="Sales bar")
        for name, value in self.data_dicto_compare:
            bar.add(name, self.date_list, value, is_label_show=False, is_datazoom_show=True, is_toolbox_show=False)
        bar.render(path=self.BASE_PATH + "%s bar_datazoom.html".format(self.html_name))


if __name__ == '__main__':
    pass

