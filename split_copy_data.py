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
    for file in old_folder:
        os.remove(file)

class CopyWork:
    def __int__(self):
        a, b, c, d, e, f, g, *h = time.localtime(time.time())
        time.sleep(f)
        if g == 5 and d == 4:  # 周六早上4点开始拷
            self.NEWPATH = "{}_{}_{}_{}{}{}".format(a, b, c, "%02.f" % d, "%02.f" % e, "%02.f" % f)  # 格式化文件名
            self.OLDPATH = "E:\\n_bak"

            self.folder_file = {}  # {文件夹:{文件大小:文件}}
            self.folder_list = []  # 批量创建路径
            self.full_file = []  # 完整备份文件路径

            self.getDict()
            self.getFullFile()
            self.makePath()
            self.copyFullFile()
            self.copyDifferent()
            self.checkFolder()
            time.sleep(3600)

    def getDict(self):
        # 记录大小到字典
        for folderpath, _, filenames in os.walk(self.OLDPATH):
            self.folder_list.append(folderpath)
            self.folder_file[folderpath] = {}
            for filename in filenames:
                self.folder_file[folderpath][getsize(join(folderpath, filename))] = filename

    def getFullFile(self):
        for folderpath, file_size in self.folder_file.items():  # 挑选最大尺寸的文件到 full_file
            if 0 != len(file_size):
                size_key = max(file_size)
                self.full_file.append(join(folderpath, file_size.get(size_key)))
                self.folder_file[folderpath].pop(size_key)

    def makePath(self):
        for path in self.folder_list:  # 建好所有路径
            y = path.replace(self.OLDPATH, "y:\\" + self.NEWPATH)
            x = path.replace(self.OLDPATH, "x:\\" + self.NEWPATH)
            os.makedirs(y)
            os.makedirs(x)

    def copyFullFile(self):
        # 到此full_file[列表]里面的都是完整备份，folder_file[嵌套字典]里面的都是差异备份
        for file_path in self.full_file:
            new_path = file_path.replace(self.OLDPATH, "y:\\" + self.NEWPATH)
            shutil.copy(file_path, new_path)

    def copyDifferent(self):
        for folder_path, files in self.folder_file.items():
            for size, file in files.items():
                new_folder = folder_path.replace(self.OLDPATH, "x:\\" + self.NEWPATH)
                shutil.copy(join(folder_path, file), join(new_folder, file))

    def checkFolder(self):
        # 校验一下，就删除源文件
        old_folder = [join(path, file) for path, _, files in os.walk(self.OLDPATH) for file in files]
        old_size = [getsize(file) for file in old_folder]
        y_f = [getsize(join(path, file)) for path, _, files in os.walk("y:\\" + self.NEWPATH) for file in files]
        x_f = [getsize(join(path, file)) for path, _, files in os.walk("x:\\" + self.NEWPATH) for file in files]
        if sum(old_size) == sum(y_f + x_f):
            deleteOldFile(old_folder)
        else:
            print("异常，请重新执行", self.NEWPATH)

def main():
    while True:
        CopyWork()

if __name__ == '__main__':
    main()
