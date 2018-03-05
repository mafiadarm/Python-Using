#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  14:16
    File Name:      /GitHub/make_folder
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import time
import os

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

def creatFolderName():
    a, b, c, d, e, f, g, *h = time.localtime(time.time())
    folder_name = "{}_{}_{}_{}{}{}".format(a, b, c, "%02.f" % d, "%02.f" % e, "%02.f" % f)
    return folder_name

def creatNewFolder(file_path):
    path, file = os.path.split(file_path)
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    pass

