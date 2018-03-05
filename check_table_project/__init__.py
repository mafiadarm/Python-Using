#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_28_2018  11:40
   File Name:      /GitHub/__init__
   Creat From:     PyCharm
   Python version: 3.6.2  
- - - - - - - - - - - - - - - 
   Description:
   1、OA 的当月请假记录
   2、考勤表异常记录
   3、提取在职人员对应的数据
        参考[当月工作时间表][在职员工信息表][考勤记录异常表][请假表][未打卡说明]
        维护一张以workingday.xlsx命名的excel表，内容为从第二行开始为每月日期
            删除或增加假期即可
        维护一张在职员工信息表，内容从第一行第一列开始（可以把现在的共享表复制到当前文件夹使用）
            第二列为工号、第四列为考勤种类
==============================
"""

import logging

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


import os
import datetime
import xlrd



