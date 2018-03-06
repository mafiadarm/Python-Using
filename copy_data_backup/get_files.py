#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  16:14
    File Name:      /GitHub/get_files
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


def getFileList(folder_path):
    """
    from folder path get all of file's path and return a list
    :param folder_path:
    :return:
    """
    file_path_list = []
    if os.path.exists(folder_path):
        for path, _, files in os.walk(folder_path):
            if not files:
                continue
            for file in files:
                file_path_list.append(os.path.join(path, file))
    return file_path_list

def getSmallFilesList(file_list):
    """
    extract file size less than and equal to 50M
    :param file_list:
    :return: list
    """
    small_list = []
    for file in file_list:
        if os.path.getsize(file) <= 50000000:  # bit
            small_list.append(file)
    return small_list

def getBiggerFileList(file_list):
    """
    extract file size great than 50M
    :param file_list:
    :return: list
    """
    bigger_list = []
    for file in file_list:
        if os.path.getsize(file) > 50000000:  # bit
            bigger_list.append(file)
    return bigger_list

if __name__ == '__main__':
    pass
