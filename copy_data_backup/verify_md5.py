#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_13_2018  14:28
    File Name:      /GitHub/md5
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""
import hashlib
import logging

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

def getFileMD5(filename):
    hh = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            byte = f.read(8096)
            if not byte:
                break
            hh.update(byte)
        f.close()
    return hh.hexdigest()

def getBytesMD5(ss):
    ss = ss.encode()
    hh = hashlib.md5(ss)
    return hh.hexdigest()