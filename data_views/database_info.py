#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_20_2018  9:48
    File Name:      /GitHub/database_info
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    连接服务器的信息
    可以用函数进行交互式的链接
    可以把设置好的数据写成dict保存
    可以调取类，设置默认值

    工业环境调用类即可
==============================
"""

__author__ = 'Loffew'

import os


class MakeDatabaseInfo:
    """
    鉴于保密问题，前置一个配置文件到固定位置，如果有就直接取，如果没有就新建
    四种方式建立这个数据，[encoding="utf-8"]
        1 实例化类，初始化数据，用createInfo生成，值类型为string
        2 先用createInfo生成文件，用getInfo读取
        3 调用getInfo，如果没有文件，则调用createInfo生成
        4 初始化initInfo
    文件的默认名为 dbf.txt
    调用时，取BASE_DB 的值
    """
    def __init__(self):
        self.server = None
        self.user = None
        self.password = None
        self.database = None
        self.BASE_DB = {}

        self.basePT = None  # sqlserver login info files path

    def getPath(self):
        if not self.basePT:
            self.basePT = os.getcwd()
        return os.path.join(self.basePT, "dbf.txt")

    def createInfo(self):
        path = self.getPath()
        print("There have not specifies file, create now!")
        with open(path, "a") as ww:
            ww.write("server = %s\n" % input("server IP = "))
            ww.write("user = %s\n" % input("username = "))
            ww.write("password = %s\n" % input("password = "))
            ww.write("database = %s\n" % input("database = "))
        print("BATH_PATH is %s" % path)

    def getInfo(self):
        path = self.getPath()
        if not os.path.exists(path):
            self.createInfo()
        with open(path, "r") as rr:
            for i in rr.readlines():
                i = i.replace("\n", "").replace(" ", "")
                i = i.split("=")
                self.BASE_DB[i[0]] = i[1]
        if self.BASE_DB.keys() != {"server", "user", "password", "database"}:
            raise ("server", "user", "password", "database")

    def initInfo(self):
        self.BASE_DB = {
            "server": self.server,
            "user": self.user,
            "password": self.password,
            "database": self.database,
        }
