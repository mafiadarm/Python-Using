#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           03_05_2018  23:31
  File Name:      /GitHub/plan
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  Time and Plan relate
==============================
"""
import logging
import time
import datetime
import calendar
from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


def timestamp(t):
    """
    format time to "%Y-%m-%d %H:%M:%S" and let it be timestamp
    :param t: like "2018-09-09 12:00:00"
    :return: a timestamp of int
    """
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timeArray))


def sleep_second():
    """
    Target is SATURDAY 12:00:00
    From now to target time, count seconds and sleep in
    :return:
    """
    target_day = datetime.date.today()
    one_day = datetime.timedelta(days=1)

    while target_day.weekday() != calendar.SATURDAY: target_day += one_day
    target_day = target_day.strftime("%Y-%m-%d")

    target = "{} 12:00:00".format(target_day)[:19]
    now = str(datetime.datetime.now())[:19]

    diff = timestamp(target) - timestamp(now)

    print("The next copy at next SATURDAY 12:00:00\nPROCESS:")
    time.sleep(0.01)
    [time.sleep(1) for _ in tqdm(range(diff))]

if __name__ == '__main__':
    pass


