#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  15:51
    File Name:      /GitHub/delete_folder
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    delete copied files and logging to log file
==============================
"""

import logging
import os
from tqdm import tqdm

__author__ = 'Loffew'

logging.basicConfig(level=logging.WARNING, format=" %(asctime)s - %(levelname)s - %(message)s", filename="log.txt")

# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def deleteFiles(file_path_list):
    """
    Delete file in list
    :param file_path_list: a list have file_path
    :return:
    """
    if not file_path_list:
        print("there is no files will to be delete.\n")
        return
    else:
        for file in tqdm(file_path_list):
            os.remove(file)
            pp_dbg("Delete %s\n" % file)

        print("DELETE END\n")


if __name__ == '__main__':
    pass













