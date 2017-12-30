import time
import shutil
import os
import datetime
from os.path import join, getsize

'''
shutil 复制文件 shutil.copyfile
os.path.exists, os.path.makedirs, os.path.mkdir, os.remove
join(path, file) getsize(file)
'''
'''
区分 日备 周备【文件是已经备份好了的情况下】
日备拷贝在2点进行
周备拷贝在5点进行
从E盘复制到对应盘 【拷贝只会对关闭的文件做动作】
    遍历E文件夹，写进列表，一个一个的提出来复制到目标
        判断是否有该文件夹，如没有，新建其
        如果有，就直接复制过去
    复制一个，校验大小，相等则复制成功，写进日志

校验E盘所有文件，是否都拷贝到对应盘
    再次生成
    如果没有，重新执行copy[自动覆盖]

写入日志，并拷贝到目标盘
'''


class CopyWork(object):
    def __init__(self, logg_text, from_source_folder, target_folder):
        self.log = logg_text
        self.SourceFolder = from_source_folder
        self.TargetFolder = target_folder
        self.file_names = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]

        self.ready_copy()
        self.check_folder()

    def ready_copy(self):
        print("\n-*- For Ready Copy -*-\n")
        for source_file_name in self.file_names:
            target_path = os.path.split(source_file_name)[0].replace(self.SourceFolder, self.TargetFolder)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            self.doing_copy(source_file_name)

    def doing_copy(self, source_file_name):
        print("\n-*- Start Copy File [%s] -*-\n" % source_file_name)
        target_file_name = source_file_name.replace(self.SourceFolder, self.TargetFolder)
        shutil.copyfile(source_file_name, target_file_name)
        if getsize(source_file_name) == getsize(target_file_name):
            print("-*- Already Copy and Success -*-\n")
            pass
        else:
            print("-*- Something Wrong and Copy Again -*-\n")
            self.doing_copy(source_file_name)

    def check_folder(self):
        print("-*- Check File of All -*-\n")
        source_folder_files = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]
        source_folder_size = sum([getsize(file) for file in source_folder_files])
        target_folder_size = \
            sum([getsize(join(path, file)) for path, _, files in os.walk(self.TargetFolder) for file in files])
        if source_folder_size == target_folder_size:
            print("-*- All of Files in %s and Start Write Log -*-\n" % self.TargetFolder)
            self.log_write(source_folder_size, target_folder_size)
        else:
            print("-*- Some Files Without Copy -*-\n")
            difference = list(set(source_folder_files) - set(self.file_names))
            for source_file_name in difference:
                print("-*- %s Files in Plan -*-\n" % len(difference))
                self.doing_copy(source_file_name)

    def log_write(self, source_size, target_size):
        notice = ("[{}] from：{}\n[{}] from：{}\n".format(source_size, self.SourceFolder, target_size, self.TargetFolder))
        with open(self.log, "a+") as logg:
            logg.write(notice)
        if not os.path.exists(join(self.TargetFolder, "log.txt")):
            print("-*- Copy log.txt to %s -*-\n" % self.TargetFolder)
            shutil.copyfile(self.log, join(self.TargetFolder, "log.txt"))
            os.remove(self.log)


if __name__ == '__main__':
    print("Start From ", datetime.datetime.now().strftime("%c"))
    while True:
        logg_Text = "E:\\log.txt"
        source_folder = "E:\\n_bak"
        a, b, c, d, e, f, g, *h = time.localtime(time.time())
        folder_name = "{}_{}_{}".format(a, b, c)
        target_folder_x = "x:\\" + folder_name
        target_folder_y = "y:\\" + folder_name
        if d == 2 and getsize(source_folder):
            start_copy = CopyWork(logg_Text, source_folder, target_folder_x)
        elif d == 5 and getsize(source_folder):
            start_copy = CopyWork(logg_Text, source_folder, target_folder_y)
        time.sleep(1800)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
