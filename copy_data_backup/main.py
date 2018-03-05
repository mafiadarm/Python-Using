#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  13:26
    File Name:      /GitHub/main
    Creat From:     PyCharm
    Python version: 3.6.2
- - - - - - - - - - - - - - - 
    Description:
    Already creat x and y in backup server.
    Copy set process:
        Make a folder named datetime in x and y.
        Split filename to get date.
            If date is Monday and in this week: pass, else copy file to y.
            If date is Tuesday to Saturday in this week: pass, else copy to x.
            Get source path and targe path to list.
                If size greater than 50M, in a list, other size in a list
        Copy small file be Threading pool first.
        Copy bigger file be Threading.
        Check file in MD5, if error, copy again.
        Delete source files.
==============================
"""

import logging
from days_list import getFileDate, getThisWeeksRange, getWeekDay
from check_folder import checkXY
from make_folder import creatFolderName
from get_files import getFileList, getBiggerFileList, getSmallFilesList
from copy_files import copyFile
from delete_folder import deleteFiles
from multiprocessing.dummy import Pool
from tqdm import tqdm

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

def close(pool):
    pool.close()
    pool.join()


if __name__ == '__main__':
    while not checkXY():
        input("If folder is ready, press any key.")

    small = Pool()
    big = Pool()

    this_week = getThisWeeksRange()

    name = creatFolderName()
    x_name = "x:/" + name
    y_name = "y:/" + name
    source_folder = "e:/n_bak"

    all_file_list = getFileList(source_folder)
    other_week_files = [file for file in all_file_list if getFileDate(file) not in this_week]

    big_list = getBiggerFileList(other_week_files)
    small_list = getSmallFilesList(other_week_files)

    for file in tqdm(small_list):
        if not getWeekDay(getFileDate(file)): f_name = y_name
        else: f_name = x_name
        small.apply_async(copyFile, args=(file, source_folder, f_name,))
        print(file)
    close(small)

    for file in tqdm(big_list):
        if not getWeekDay(getFileDate(file)): f_name = y_name
        else: f_name = x_name
        copyFile(file, source_folder, f_name,)
        print(file)

    big_list.extend(small_list)
    deleteFiles(big_list)