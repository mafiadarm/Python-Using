#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_20_2018  11:38
    File Name:      /pychart_SqlServer/main
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    在此添加数据处理方法，因为视图获取的数据多样性，需要不同的数据处理方法，结果的格式是可以共用的，字典也设置为有序
==============================
"""

from sql_query import SqlConnect
from collections import OrderedDict as Dict
import datetime

__author__ = 'Loffew'


class MakeData:
    def __init__(self):
        """
        self.database 连接的数据库
        self.fields 查询返回的列名，默认为"*"
        self.datatable 查询的表名 比如 "ROSUNDB.dbo.zy"， "ROSUNDB.dbo.dl"，在数据库查看
        self.condition 查询需要的条件
        具体sql语法，语句查看[http://www.runoob.com/sql/sql-tutorial.html]
        """
        self.database = None
        self.fields = None
        self.datatable = None
        self.condition = None
        self.data = [[1,2],[3,4]]

        self.name = None
        self.year = None

        self.data_dict = Dict()
        self.data_dicto_compare = Dict()
        self.data_list = []
        self.date_list = []
        self.x_list = []
        self.y_list = []

    def data_return(self):
        """
        具体的sql语法查看http://www.runoob.com/sql/sql-tutorial.html

        name: 生成的html的title前缀
        database: 数据库的连接信息，必须是dict格式
        fields: 必须是string格式
        datatable: 必须是string格式 必须是有效数据表
        condition: 必须是string格式
        year: 数字格式，以获取当年的日历,默认获取2018年日历
        :return: 生成一个字典后，在当前文件夹生成日历热点图
        """
        if not self.database: return "check your database!"
        if not self.fields: self.fields = "*"
        if not self.datatable: return "There is no table?"

        sql = "SELECT " + self.fields + " FROM " + self.datatable
        if self.condition:
            sql += " WHERE " + self.condition

        c = SqlConnect(self.database)
        self.data = c.query_data(sql)

    def make_data_dict(self, name_list=None):
        """
        汇总2 项对应关系，形成dict
        :return: [k:v]
        """
        self.data_dict.clear()
        try:
            for k, v in self.data:
                if name_list:
                    k = self.return_name(k, name_list)
                if k in self.data_dict:
                    self.data_dict[k] += float(v)
                else:
                    self.data_dict[k] = float(v)
        except Exception as e:
            print("day_sales_hot_calendar error! there must be dict={date:digit}")
            raise e

    @staticmethod
    def return_name(name, name_list):
        for i in name_list:
            if i in name:
                return i

    def make_data_three_dict(self, name_list=None):
        for k, v, z in self.data:
            if name_list:
                k = self.return_name(k, name_list)
            if k in self.data_dict:
                if v in self.data_dict[k]:
                    self.data_dict[k][v] += float(z)
                else:
                    self.data_dict[k][v] = float(z)
            else:
                self.data_dict[k] = {v: float(z)}

    def make_date_list(self, start, end=None):
        """
        获取一个日历列表
        :return: [year_month_day] example: "2018-12-31"
        """
        self.date_list.clear()

        begin_day = datetime.date(start, 1, 1)
        if not end:
            end_day = datetime.date.today()
        else:
            end_day = datetime.date(end, 12, 31)

        add_oneday = datetime.timedelta(1)

        while begin_day <= end_day:
            self.date_list.append(str(begin_day))
            begin_day += add_oneday

    def make_day_sales_calendar(self):
        """
        某个点上面，因为数据过大，影响数据展示，可以考虑设置为0，去掉注释即可
        data_dict[max(data_dict, key=int)] = 0  # 去掉最后一天
        data_dict[max(data_dict, key=data_dict.get)] = 0  # 去掉最大数字
        :return: {date: value}
        """
        pass

    def make_trim_suffix(self):
        """
        对self.data_list进行修剪，去掉省或市后的名字，对应该区域的数据
        :return: [area: value]
        """
        self.data_list = [(k.replace("省", "").replace("市", ""), v) for k, v in self.data_dict.items()]

    def make_for_bar_3D_month(self):
        """
        按月计算[2018-01]，对应每月数据[汇总结果]： 汇总结果取于data_dict.value
        生成数据为：
            self.data_list=[index(day_month), index(year), value]
            self.y_list=[years]
            self.x_list=[months]
        """
        for day, money in self.data_dict.items():
            day_tuple = (int(day[4:6])-1, int(day[:4])-self.year)
            if day_tuple in self.data_dicto_compare:
                self.data_dicto_compare[day_tuple] += money
            else: self.data_dicto_compare[day_tuple] = money

        self.data_list = [[day[0], day[1], money] for day, money in self.data_dicto_compare.items()]
        self.y_list = sorted(list({day[:4] for day in self.data_dict.keys()}))
        self.x_list = ["{}月".format(i) for i in range(1, 13)]

    def make_for_bar_3D_day(self):
        """
        按1年为周期，按日计算
        从get_date_list(begin, end) 预构成一个闰年的日期的列表
        get_date_list默认生成的数据为["2018-01-01"]，需要更新格式为["0101"]
        data_list的数据需要date_list的index支持，如果没有，可能报错超出范围
        生成数据为：
            data_list=[index(month_day), index(year), value], y_list=[years]
            date_list=[month_day, month_day] 此项用于x轴[x_list]
            self.y_list=[year_month, year_month]
        """
        self.make_date_list(2000, 2000)
        self.date_list = [day.replace("-", "")[4:] for day in self.date_list]
        self.data_list = [[self.date_list.index(day[4:]), int(day[:4]) - self.year, money]
                          for day, money in self.data_dict.items()]
        self.y_list = sorted(list({day[:4] for day in self.data_dict.keys()}))
        self.x_list = self.date_list

    def make_summary_day_to_money(self):
        """
        获取每天对应的数据
        从get_date_list(begin, end) 预构成一个从开始到结束的日期的列表，元素为 [year_month_day] example: "20180101"
            get_date_list默认生成的数据为["2018-01-01"]，需要更新格式为["20180101"]
        data_list的数据需要date_list的index支持，如果没有，可能报错超出范围
        支持 重复执行，即可叠加数据的功能，可对比
        :return:  self.date_list=[day: [moneys]]
        """
        ll = [0] * len(self.date_list)
        for k in sorted(self.data_dict.keys()):
            ll[self.date_list.index(k)] = self.data_dict.get(k)

        self.data_dicto_compare[self.name] = ll


if __name__ == '__main__':
    pass
