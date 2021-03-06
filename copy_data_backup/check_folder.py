#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  14:00
    File Name:      /GitHub/check_folder
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import os


__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def checkXY():
    """
    Check x and y whether creat or connect
    True have condition both of xy
    :return:
    """
    if os.path.exists("x:/") and os.path.exists("y:/"):
        return True
    print("Please check x: and y:")
    return False


def getAllFile(*args):
    fileList = []
    for folder in args:
        fileList.extend([os.path.join(p, f) for p, _, fs in os.walk(folder) for f in fs])
    return fileList


if __name__ == '__main__':
    pass






