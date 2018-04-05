#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_27_2018  9:19
    File Name:      /e_mail_send_payroll/stuff_email
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    从员工信息的excel里面读取员工对应的邮箱，只获取工号和邮箱
==============================
"""

import logging
import xlrd
import os
import re

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


class Stuff:
    def __init__(self):
        self.stuff_info = {}

    def get_email_addr(self):
        text = re.compile(r"^RX\d{5}|\w+@rosun.com.cn$")
        if os.path.exists("员工信息.xlsx"):
            data = xlrd.open_workbook("员工信息.xlsx", "r")
            form = data.sheet_by_index(0)
            rows = form.nrows
            for i in range(rows):
                get = [i for i in form.row_values(i) if text.findall(str(i))]
                if len(get) == 2:
                    self.stuff_info[get[0]] = get[1]
        else:
            input("当前文件夹没有《员工信息.xlsx》,按回车键退出")
            quit()
