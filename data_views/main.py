#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_21_2018  14:19
    File Name:      /pychart_SqlServer/query_connect
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    调取make.html接口，立即生成html
    如果需要在一张图增加多个数据，修改con信息后，用html.data_return(**con)和html.summary_dict()重新生成数据
==============================
"""

from views_template import *
from database_info import *


__author__ = 'Loffew'


def date_hot():
    """
    以 直营 2016年数据为例
    获取时间和发生金额，形成每日销货金额日历
    :return:
    """
    v = Views()
    # 设置数据库信息
    v.start_year = 2016  # 默认为2016
    v.database = BASE_ROSUNDB
    v.fields = ",".join((dbt_date, dbt_total_price,))
    v.datatable = "ROSUNDB.dbo.zy"
    v.condition = "{}>={}0101 and {}<={}1231".format(dbt_date, 2016, dbt_date, 2016)
    # 获取数据-汇总
    v.data_return()
    v.make_data_dict()
    v.make_date_list(2016, 2016)
    # 数据清洗
    v.data_dict = [[day, v.data_dict.get(day.replace("-", ""), 0)] for day in v.date_list]
    # 渲染成html文件
    v.table_name = "直营"
    v.html_name = "_zy"
    v.view_date_hot()


def bar_3D():
    """
    以 直营 2016年数据为例，制作为按月为单位和按日为单位的3D图形
    获取时间和发生金额，生成3D图形
    :return:
    """
    v = Views()
    # 设置数据库信息
    v.year = 2015
    v.start_year = 2015
    v.database = BASE_ROSUNDB
    v.fields = ",".join((dbt_date, dbt_total_price,))
    v.datatable = "ROSUNDB.dbo.zy"
    v.condition = "{}>={}0101 and {}<={}1231".format(dbt_date, 2015, dbt_date, 2017)
    # 获取数据-汇总
    v.data_return()
    v.make_data_dict()
    # 对数据清洗
    v.make_for_bar_3D_month()
    # 生成html文件
    v.html_name = "zy_month"
    v.table_name = "直营[月]"
    v.view_bar_3D()
    # 再次生成数据
    v.make_for_bar_3D_day()
    v.html_name = "zy_day"
    v.table_name = "直营[日]"
    v.view_bar_3D()


def block_area():
    """
    以 直营 2016年数据为例，制作全国范围内的区域色块
    获取金额和地域名，生成块状颜色地图
    :return:
    """
    v = Views()
    # 设置数据库信息
    v.start_year = 2016
    v.database = BASE_ROSUNDB
    v.fields = ",".join((dbt_province, dbt_total_price,))
    v.datatable = "ROSUNDB.dbo.zy"
    v.condition = "{}>={}0101 and {}<={}1231".format(dbt_date, 2016, dbt_date, 2016)
    # 获取数据-汇总
    v.data_return()
    v.make_data_dict()
    # 对数据清洗
    v.make_trim_suffix()
    # 生成html文件
    v.table_name = "直营"
    v.html_name = "_zy"
    v.view_block_area_map()


def grow_compare():
    """
    此图尽量限制在1个月以内比较好展现
    :return:
    """
    pass


def datazoom_bar():
    """
    以直营和代理 2016-2017 每天的总数据为例
    比较多条数据，以竖条的形式产生
    获取时间和总金额，生成区域可选的图标
    :return:
    """
    v = Views()
    # 设置数据库信息
    v.database = BASE_ROSUNDB
    v.fields = ",".join((dbt_date, dbt_total_price,))
    v.datatable = "ROSUNDB.dbo.zy"
    v.condition = "{}>={}0101 and {}<={}1231".format(dbt_date, 2015, dbt_date, 2017)
    # 获取数据-汇总
    v.data_return()
    v.make_data_dict()
    # 获取支持参数
    v.make_date_list(2015, 2017)
    v.date_list = [day.replace("-", "") for day in v.date_list]
    # 数据清洗
    v.name = "直营"
    v.make_summary_day_to_money()

    # 修改数据表，其他信息都一样
    v.datatable = "ROSUNDB.dbo.dl"
    # 获取数据-汇总
    v.data_return()
    v.make_data_dict()
    # 数据清洗
    v.name = "代理"
    v.html_name = "代理 and 直营"
    v.make_summary_day_to_money()

    # 生成html文件
    v.html_name = "zy_dl_"
    v.view_bar_datazoom()


def pie():
    """
    以2016年 各部门业绩比例为例
    以日期获取部门和金额，展示饼图
    :return:
    """
    v = Views()
    # 设置数据库信息
    v.year = 2016
    v.database = BASE_ROSUNDB
    v.fields = ",".join((dbt_depart, dbt_total_price,))
    v.datatable = "ROSUNDB.dbo.zy"
    v.condition = "{}>={}0101 and {}<={}1231".format(dbt_date, 2016, dbt_date, 2016)
    # 获取数据-汇总
    v.data_return()
    v.make_data_dict(name_list=["水王子", "大众健康", "公共卫生", "国际业务", "销售服务", "工业"])
    # 数据清洗

    # 生成html文件
    v.table_name = "直营"
    v.html_name = "zy"
    v.view_data_of_pie()


if __name__ == '__main__':
    db = MakeDatabaseInfo()
    db.basePT = "C:/Users/lo/Desktop/"
    db.getInfo()
    BASE_ROSUNDB = db.BASE_DB

    date_hot()
    # bar_3D()
    # block_area()
    # datazoom_bar()
    # pie()
