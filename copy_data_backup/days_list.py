#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  16:17
    File Name:      /GitHub/days_list
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import re
import datetime

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def getWeekDay(func):
    def week(*args, **kwargs):
        return datetime.datetime.strptime(func(*args, **kwargs), "%Y%m%d").weekday()  # [0-6]
    return week


@getWeekDay
def getFileDate(filename):
    regx = re.compile(r'.*backup_([0-9_]{10}).*')
    date = regx.findall(filename)[0]
    return date.replace("_", "")


@getWeekDay
def getTodayWeek():
    return str(datetime.date.today()).replace("-", "")


def getThisWeeksRange():
    week = datetime.date.today()
    year, month, day = str(week).split("-")
    year, month, day = int(year), int(month), int(day)
    flag = datetime.date(year, month, day).weekday()

    while flag:
        day -= 1
        flag = datetime.date(year, month, day).weekday()

    start_day = str(datetime.date(year, month, day))
    start_day = int(start_day.replace("-", ""))
    return [str(start_day + i) for i in range(6)]

if __name__ == '__main__':
    pass
