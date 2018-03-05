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

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def copyFile(file, source, targ):
    new_file = file.replace(source, targ)
    creatNewFolder(new_file)
    shutil.copyfile(file, new_file)