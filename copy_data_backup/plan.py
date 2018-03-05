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
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timeArray))


def sleep_second():
    target_day = datetime.date.today()
    one_day = datetime.timedelta(days=1)

    while target_day.weekday() != calendar.SATURDAY: target_day += one_day
    target_day = target_day.strftime("%Y-%m-%d")

    target = "{} 4:00:00".format(target_day)[:19]
    now = str(datetime.datetime.now())[:19]

    diff = timestamp(target) - timestamp(now)

    print("The next copy progress is:")
    [time.sleep(1) for t in tqdm(range(diff))]



