import time
import shutil
import os
import datetime
from os.path import join, getsize

'''
shutil.copyfile
os.path.exists, os.path.makedirs, os.path.mkdir, os.remove
join(path, file) getsize(file)
'''


class CopyWork(object):
    def __init__(self, logg_text, from_source_folder, target_folder):
        self.log = logg_text  # 日志文件路径
        self.SourceFolder = from_source_folder  # 源文件夹
        self.TargetFolder = target_folder  # 目标文件夹
        self.file_names = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]  # 最初的准备复制的列表
        self.log_messages = []  # 把日志信息先放到列表里面

        self.ready_copy()
        self.check_folder()

    def ready_copy(self):
        print("\n-*- For Ready Copy to %s -*-\n" % self.TargetFolder)
        for source_file_name in self.file_names:  # 遍历准备复制的列表[文件全路径]
            self.doing_copy(source_file_name)

    def doing_copy(self, source_file_name):  # 处理复制文件
        print("-*- Start Copy File [%s] -*-\n" % source_file_name)
        target_file_name = source_file_name.replace(self.SourceFolder, self.TargetFolder)  # 目标文件全路径
        target_path = os.path.split(source_file_name)[0].replace(self.SourceFolder, self.TargetFolder)  # 目标文件夹全路径
        if not os.path.exists(target_path):  # 判断是否有路径
            os.makedirs(target_path)  # 没有就新建
        shutil.copyfile(source_file_name, target_file_name)  # 复制文件
        if getsize(source_file_name) == getsize(target_file_name):  # 如果两边文件相等
            print("-*- %s Already Copy and Success -*-\n" % source_file_name)
            self.log_messages.append("[{}] Already Copy From {}\n".format(getsize(source_file_name), source_file_name))  # 写入日志
            pass
        else:  # 如果两边不相等
            print("-*- Something Wrong and Copy Again -*-\n")
            self.doing_copy(source_file_name)  # 重新复制

    def check_folder(self):  # 检查两边文件夹
        print("-*- Check File of All -*-\n")
        source_folder_files = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]  # 现在源文件夹内所有文件路径
        source_folder_size = sum([getsize(file) for file in source_folder_files])  # 现源文件夹大小
        target_folder_size = \
            sum([getsize(join(path, file)) for path, _, files in os.walk(self.TargetFolder) for file in files])  # 目标文件夹大小
        if source_folder_size == target_folder_size:  # 如果两边文件夹大小一样
            print("-*- All of Files in %s and Start Write Log -*-\n" % self.TargetFolder)
            self.log_write(source_folder_size, target_folder_size)  # 把结果写入日志
            print("-*- Delete Source Files -*-\n")
            for delete_file in source_folder_files:  # 遍历源文件夹
                os.remove(delete_file)  # 删除文件
        else:  # 如果两边文件夹大小不一样
            if os.path.exists(join(self.TargetFolder, "log.txt")):  # 如果目标文件夹内已经生成日志
                print("\n-*- Delete Redundant Log File -*-\n")
                os.remove(join(self.TargetFolder, "log.txt"))  # 先删除日志
            print("-*- Some Files Without Copy -*-\n")
            difference = list(set(source_folder_files) - set(self.file_names))  # 计算差了那些文件
            print("-*- %s Files in Plan -*-\n" % len(difference))
            for source_file_name in difference:  # 遍历差出来的文件列表
                self.doing_copy(source_file_name)  # 复制
            self.check_folder()  # 再检查

    def log_write(self, source_folder_size, target_folder_size):
        self.log_messages.append("[{}] from：{}\n[{}] from：{}\n".format(source_folder_size, self.SourceFolder, target_folder_size, self.TargetFolder))  # 比较信息写入日志
        with open(self.log, "a+") as logg:  # 打开日志文件[自动关闭]
            logg.writelines(self.log_messages)  # 写入日志[把list中的字符串一行一行地写入]
        if not os.path.exists(join(self.TargetFolder, "log.txt")):  # 如果当前目标文件夹没日志
            print("-*- Copy log.txt to %s -*-\n" % self.TargetFolder)
            shutil.copyfile(self.log, join(self.TargetFolder, "log.txt"))  # 复制日志到目标文件夹
            os.remove(self.log)  # 删除原文件夹


if __name__ == '__main__':
    print("Start From ", datetime.datetime.now().strftime("%c"))
    while True:
        logg_Text = "E:\\log.txt"
        source_folder = "E:\\n_bak"
        a, b, c, d, e, f, g, *h = time.localtime(time.time())
        folder_name = "{}_{}_{}_{}{}{}".format(a, b, c, "%02.f" % d, "%02.f" % e, "%02.f" % f)  # 格式化文件名
        target_folder_x = "x:\\" + folder_name
        target_folder_y = "y:\\" + folder_name
        source_size = sum([getsize(join(path, file)) for path, _, files in os.walk(source_folder) for file in files])  # 计算源文件夹大小[触发]
        if d == 2 and source_size:  # 如果在2点，源文件夹如果有数据
            start_copy = CopyWork(logg_Text, source_folder, target_folder_x)  # 实例化
        elif d == 5 and g == 5 and source_size:  # 如果在5点，源文件如果有数据
            start_copy = CopyWork(logg_Text, source_folder, target_folder_y)  # 实例化
        time.sleep(1800)  # 休息半小时
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
