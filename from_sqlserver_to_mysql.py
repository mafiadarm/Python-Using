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
==============================
"""
import pymssql
import os

import pymysql

__author__ = 'Loffew'


class SqlConnect:
    def __init__(self, database):
        try:
            self.conn = pymssql.connect(**database, charset="GBK")
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

        assert self.BASE_DB.keys() != {"server", "user", "password", "database"}, \
            "error: please check server user password database!"


class ConnectPackage:
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
            # Commit to database execution.
            self.conn.commit()
        except Exception:
            # Rollback in case there is any error
            self.conn.rollback()
        finally:
            self.connClose()


if __name__ == '__main__':
    info = MakeDatabaseInfo()
    info.basePT = "C:/Users/lo/Desktop/"
    info.getInfo()

    cp = ConnectPackage()
    datatable = "ROSUNDB.dbo.zy"
    sql_fields = [  # 年份 品号 单位 单价 总价 地址1 地址2 省份 客户 部门 员工
        cp.date, cp.number,
        cp.unit, cp.per_unit,
        cp.add1, cp.add2,
        cp.total_price, cp.province,
        cp.client, cp.depart,
        cp.saler,
    ]

    sql_sentence = "SELECT " + ",".join(sql_fields) + " FROM " + datatable + " WHERE " + cp.date + " >= 20150101"

    sql_connect = SqlConnect(info.BASE_DB)
    data = sql_connect.query_data(sql_sentence)  # list格式

    mysql_data_info = {
        "host": "localhost",
        "username": "root",
        "password": "1",
        "database": "SellProxyInfo"
    }

    mysql_sentence = "INSERT INTO SellProxyInfo  VALUES ({},{},{},{},{},{},{},{},{},{},{})"

    mysql_connect = MysqlUse(**mysql_data_info)

    for d in data:
        n = [x.strip() if d.index(x) != 3 and d.index(x) != 4 else x for x in d]
        mysql_connect.executeCommit(mysql_sentence.format(*n))

