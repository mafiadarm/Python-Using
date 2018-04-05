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
    This py is about get when creat in filename.
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
    """
    Get week day
    :param func: any function
    :return: [0-6]
    """
    def week(*args, **kwargs):
        return datetime.datetime.strptime(func(*args, **kwargs), "%Y%m%d").weekday()
    return week


def getFileDate(filename):
    """
    Use re module to get info.
    Get datetime that create file in filename.
    :param filename:
    :return: like "20180909"
    """
    regx = re.compile(r'.*backup_([0-9_]{10}).*')
    date = regx.findall(filename)[0]
    return date.replace("_", "")


def getFileWeek(filename):
    """
    Example:
        Filename format like ROSUNCAIWU_backup_2018_03_09_013001_4402415
        Get 2018-03-09 then get the week
    :param filename:
    :return: [0 - 6]
    """
    return getWeekDay(getFileDate)(filename)


@getWeekDay
def getTodayWeek():
    """
    Use string to get a datetime
    :return: like "2018-09-09"
    """
    return str(datetime.date.today()).replace("-", "")


def getThisWeeksRange():
    """
    :return: this week days in list
    """
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
