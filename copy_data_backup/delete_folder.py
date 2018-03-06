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
==============================
"""

import logging
import os
from multiprocessing.dummy import Pool

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

files = Pool()

def deleteFiles(file_path_list):
    """
    Delete file of file_path_list in Threading pool
    :param file_path_list: a list have file_path
    :return:
    """
    if not file_path_list:
        print("there is no files will to be delete.\n")
        return
    else:
        [files.apply_async(os.remove, args=(file,)) for file in file_path_list]
        files.close()
        files.join()
        print("DELETE END\n")


if __name__ == '__main__':
    pass













