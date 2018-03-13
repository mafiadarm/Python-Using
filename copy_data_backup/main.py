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
        Copy bigger file be in Order.
        Check file in MD5, if error, copy again.[undo]
        Delete source files.
==============================
"""

import logging

import time
from days_list import getFileDate, getThisWeeksRange, getTodayWeek, getFileWeek
from check_folder import checkXY
from make_folder import creatFolderName
from get_files import getFileList, getBiggerFileList, getSmallFilesList
from copy_files import copyFile
from delete_folder import deleteFiles
from plan import sleep_second
from multiprocessing.dummy import Pool
from tqdm import tqdm

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def close(pool):
    """
    Guard pool process
    In order [close and join]
    :param pool: pool variable name
    :return:
    """
    pool.close()
    pool.join()


def file_name(file):
    """
    Ues week code [0-6] decide file name.
    File name decide files where to go.
    :param file:
    :return: finally target
    """
    if not getFileWeek(file): f_name = y_name
    else: f_name = x_name
    return f_name


def main():
    other_week_files = [file for file in getFileList(source_folder) if getFileDate(file) not in getThisWeeksRange()]
    if not other_week_files and getTodayWeek() == 5: other_week_files = getFileList(source_folder)

    big_list = getBiggerFileList(other_week_files)
    small_list = getSmallFilesList(other_week_files)

    print("SMALL FILE PROCESS")
    time.sleep(0.5)
    for file in tqdm(small_list):
        f_name = file_name(file)
        small.apply_async(copyFile, args=(file, source_folder, f_name,))
    close(small)

    print("BIG FILE PROCESS")
    time.sleep(0.5)
    for file in tqdm(big_list):
        f_name = file_name(file)
        copyFile(file, source_folder, f_name)

    big_list.extend(small_list)
    deleteFiles(big_list)

    time.sleep(0.5)
    sleep_second()

if __name__ == '__main__':
    while True:
        while not checkXY():
            input("If folder is ready, Press Enter")

        small = Pool()

        source_folder = "e:/n_bak"
        name = creatFolderName()
        x_name = "x:/" + name
        y_name = "y:/" + name

        main()