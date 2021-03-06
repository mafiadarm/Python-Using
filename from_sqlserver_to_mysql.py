#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           06_25_2018  10:38
    File Name:      /GitHub/from_sqlserver_to_mysql
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    新建database的时候，必须要用设置默认编码为utf-8
    CREATE DATABASE `name` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
==============================
"""
import pymssql
import os
import time
import pymysql

__author__ = 'Loffew'


class SqlConnect:
    def __init__(self, database):
        try:
            self.conn = pymssql.connect(**database)
            self.curr = self.conn.cursor()
        except Exception as e:
            raise e

    def close(self):
        self.curr.close()
        self.conn.close()

    def query_data(self, sql_sentence):
        try:
            self.curr.execute(sql_sentence)
            result = self.curr.fetchall()
        except Exception as e:
            raise e
        finally:
            self.close()
        return result


class MakeDatabaseInfo:
    def __init__(self):
        self.BASE_DB = {}
        self.basePT = None  # sqlserver login info files path

    def getPath(self):
        if not self.basePT:
            self.basePT = os.getcwd()
        return os.path.join(self.basePT, "dbf.txt")

    def getInfo(self):
        path = self.getPath()
        if not os.path.exists(path):
            return "ERROR: THERE IS NO SQLSERVER INFOMATION FULE"

        with open(path, "r") as rr:
            for i in rr.readlines():
                i = i.replace("\n", "").replace(" ", "")
                i = i.split("=")
                self.BASE_DB[i[0]] = i[1]

        assert self.BASE_DB.keys() == {"server", "user", "password", "database"}, \
            "error: please check server user password database!"


class ConnectPackage:  # 按实际新建类去对应数据表
    date = "COPTGTG003"
    number = "COPTHTH005"
    unit = "COPTHTH006"
    per_unit = "COPTHTH008"
    total_price = "COPTHTH013"
    add1 = "COPTCTC010"
    add2 = "COPTCTC011"
    province = "COPTCUDF02"
    agent = "COPTCUDF03"  # zy表没有此字段
    client = "COPMAMA002"
    depart = "CMSMEME002"
    saler = "CMSMVMV002"


class MysqlUse:
    def __init__(self, **kwargs):
        self.port = kwargs.get("port")
        self.host = kwargs.get("host")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.database = kwargs.get("database")

        self.conn = self.connect()
        self.cur = self.conn.cursor()

    def connClose(self):
        self.cur.close()
        self.conn.close()

    def connect(self):
        if not self.port: self.port = 3306
        if not self.username or not self.password:
            return pymysql.connect(host=self.host, db=self.database, port=self.port, charset='utf8')
        elif not self.database:
            return pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password, charset='utf8')
        else:
            return pymysql.connect(host=self.host, db=self.database, port=self.port, user=self.username, password=self.password, charset='utf8')

    def executeCommit(self, sql):
        """
        use sql sentence to all want
        :param sql: any sql sentence to be execution
        """
        try:
            # execute sentence
            self.cur.execute(sql)
        except Exception:
            # Rollback in case there is any error
            self.conn.rollback()


if __name__ == '__main__':
    # sqlserver登陆信息
    info = MakeDatabaseInfo()
    info.basePT = "/home/zzz/Documents"
    info.getInfo()
    # mysql登陆信息
    mysql_data_info = {
        "host": "localhost",
        "username": "root",
        "password": "1",
        "database": "rosun_sell"
    }

    # 从这个数据库获取信息
    cp = ConnectPackage()
    data_table = "ROSUNDB.dbo.zy"
    data_fields = [  # 年份 品号 单位 单价 总价 地址1 地址2 省份 客户 部门 员工
        cp.date, cp.number,
        cp.unit, cp.per_unit,
        cp.total_price, cp.add1,
        cp.add2, cp.province,
        cp.client, cp.depart,
        cp.saler,
    ]

    # 对应装数据的信息配置，要对应model里面的字段
    mysql_sentence = "INSERT INTO sell_sellproxyinfo" \
                     " (sell_date, article, unit, price, total_price, add1, add2, province, consumer, department, staff) " \
                     "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"

    sql_sentence = "SELECT " + ",".join(data_fields) + " FROM " + data_table + " WHERE " + cp.date + " >= 20150101"

    # 提取sqlserver
    try:
        sql_connect = SqlConnect(info.BASE_DB)
        data = sql_connect.query_data(sql_sentence)  # list格式
    finally:
        print("please close sql_connect.close()!")

    # 导入mysql
    try:
        mysql_connect = MysqlUse(**mysql_data_info)

        for d in data:
            # 这里要按实际变更
            n = [str(x.strip()) if d.index(x) != 3 and d.index(x) != 4 else str(x) for x in d]
            n[0] = str(f"{n[0][:4]}-{n[0][4:6]}-{n[0][6:8]}")  # 对日期单独处理
            # print(d)
            mysql_connect.executeCommit(mysql_sentence.format(*n))

        # print(mysql_sentence.format(*n))

    finally:
        print("please close mysql_connect.connClose()!")

    # 执行事物
    mysql_connect.conn.commit()

    # 关闭数据库
    sql_connect.close()
    mysql_connect.connClose()

