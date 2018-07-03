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
import os
import pymssql
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
            return pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                   charset='utf8')
        else:
            return pymysql.connect(host=self.host, db=self.database, port=self.port, user=self.username,
                                   password=self.password, charset='utf8')

    def executeSql(self, sql):
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
    pass
