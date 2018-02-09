# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_30_2018  16:23
   File Name:      /GitHub/split_copy_data
   Creat From:     PyCharm
   Python version: 3.6.2
- - - - - - - - - - - - - - - 
   Description:
   a 现在的备份计划为：周一做整备，周二到周五晚上做差异
   b 拷贝服务器备份，每周一次，每次把整备和差异分开
==============================
"""

import logging
import time
import shutil
import os
from os.path import join, getsize


__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)

def deleteOldFile(old_folder):
    print("deleteOldFile")
    for file in old_folder:
        os.remove(file)

class CopyWork:
    def __init__(self):
        a, b, c, d, e, f, g, *h = time.localtime(time.time())
        time.sleep(f)
        if g == 5 and d == 3:  # g = weeks d = hours
            print("start work")
            self.NEWPATH = "{}_{}_{}_{}{}{}".format(a, b, c, "%02.f" % d, "%02.f" % e, "%02.f" % f)
            self.OLDPATH = "E:\\n_bak"

            self.folder_file = {}  # {folder:{file:size}}
            self.folder_list = []
            self.full_file = []

            self.getDict()
            self.getFullFile()
            self.makePath()
            self.copyFullFile()
            self.copyDifferent()
            self.checkFolder()
            print("finish work")
            time.sleep(3600)

    def getDict(self):
        print("getDict")
        for folderpath, _, filenames in os.walk(self.OLDPATH):
            self.folder_list.append(folderpath)
            self.folder_file[folderpath] = {}
            for filename in filenames:
                self.folder_file[folderpath][filename] = getsize(join(folderpath, filename))

    def getFullFile(self):
        print("getFullFile")
        for folderpath, file_size in self.folder_file.items():
            if 0 != len(file_size):
                size_key = max(file_size, key=file_size.get)
                self.full_file.append(join(folderpath, size_key))
                file_size.pop(size_key)

    def makePath(self):
        print("makePath")
        for path in self.folder_list:
            y = path.replace(self.OLDPATH, "y:\\" + self.NEWPATH)
            x = path.replace(self.OLDPATH, "x:\\" + self.NEWPATH)
            os.makedirs(y)
            os.makedirs(x)

    def copyFullFile(self):
        print("copyFullFile")
        for file_path in self.full_file:
            new_path = file_path.replace(self.OLDPATH, "y:\\" + self.NEWPATH)
            shutil.copy(file_path, new_path)

    def copyDifferent(self):
        print("copyDifferent")
        for folder_path, files in self.folder_file.items():
            if 0 != len(files):
                for file, _ in files.items():
                    new_folder = folder_path.replace(self.OLDPATH, "x:\\" + self.NEWPATH)
                    shutil.copy(join(folder_path, file), join(new_folder, file))

    def checkFolder(self):
        print("checkFolder")
        old_folder = [join(path, file) for path, _, files in os.walk(self.OLDPATH) for file in files]
        old_size = [getsize(file) for file in old_folder]
        y_f = [getsize(join(path, file)) for path, _, files in os.walk("y:\\" + self.NEWPATH) for file in files]
        x_f = [getsize(join(path, file)) for path, _, files in os.walk("x:\\" + self.NEWPATH) for file in files]
        if sum(old_size) == sum(y_f + x_f):
            deleteOldFile(old_folder)
        else:
            print("Something wrong, Please again", self.NEWPATH)

def main():
    while True:
        CopyWork()

if __name__ == '__main__':
    main()