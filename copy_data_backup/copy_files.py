#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_05_2018  17:11
    File Name:      /GitHub/copy_files
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import logging
import shutil
from make_folder import creatNewFolder
from verify_md5 import getFileMD5

__author__ = 'Loffew'

logging.basicConfig(level=logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s", filename="log.txt")

# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def copyFile(file, source, targ):
    """
    Copy file to target folder
    :param file: file
    :param source: source folder
    :param targ: target folder
    :return:
    """
    new_file = file.replace(source, targ)
    creatNewFolder(new_file)
    shutil.copyfile(file, new_file)

    source_md5 = getFileMD5(file)
    target_md5 = getFileMD5(new_file)
    if source_md5 != target_md5:
        copyFile(file, source, targ)
    else: pp_dbg(("%s md5 %s\n" % (file, source_md5), "%s md5 %s\n" % (new_file, target_md5)))


