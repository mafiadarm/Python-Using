# _*_ coding:utf-8 _*_

"""
每次数据做了备份以后，要移到储存服务器
复制后，检查两边文件大小是否一致

检查文件夹是否为空
检查文件（夹）路径是否为真
检查日志文件是否存在

考虑到子目录文件和根目录文件可能重名，复制过去后会覆盖[虽然这里不会发生]，所以还要做调整
"""
import time, shutil, os, datetime
from os.path import join, getsize

class data_Maker_Work(object):
    def __init__(self, x_File, y_File, data_Back_Folder, logg_Text):
        # 定义传参
        self.x = x_File
        self.y = y_File
        self.folder = data_Back_Folder
        self.log = logg_Text


        print("开始监控", datetime.datetime.now().strftime("%c"))
        while True:  # 循环 单线程执行
            if (2 < d < 30 and self.getFileSize(self.folder) != 0) or (g == 5 and 5 < d < 6 and self.getFileSize(self.folder) != 0):
                self.sou = self.getFileSize(self.folder)
                self.plan()  # 执行plan[复制前的检查]
                self.log_doc()  # 执行日志编写
            time.sleep(1)  # 间隔
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    def plan(self):  # 只能执行一个
        if 2 < d < 30:
            print("\n-----本次复制到x盘------\n")
            for root, dirs, files in os.walk(self.folder):  # 遍历本机备份文件夹
                if files:  # 如果不为空 则执行
                    self.DataBack(self.x, files, root)
            print("\n-----复制到x盘完毕__%s------\n" % datetime.datetime.now().strftime("%c"))

        if g == 5 and 5 < d < 6:
            print("\n-----本次复制到y盘------\n")
            for root, dirs, files in os.walk(self.folder):  # 遍历本机备份文件夹
                if files:  # 如果不为空 则执行
                    self.DataBack(self.y, files, root)
            print("\n-----复制到y盘完毕------\n")
            print("\n-----开始清理文件------\n")
            self.clear_Up()
            print("\n-----清理完毕------\n")

    def DataBack(self, folder, files, root):  # 因为是两种不同情况，所以要传参进来
        if not os.path.exists(folder):  # 如果没有目标文件路径
            os.mkdir(folder)  # 新建
            print("新建文件夹：%s" % folder)

        for file in files:  # 遍历所有文件，每个文件执行一次copy
            print("\n-----准备复制%s文件-----\n" % file)
            self.testFileSccess(file, folder, root)

    def testFileSccess(self, file, folder, root):
        print("-----现在开始复制---[%s]---\n" % self.getFileSize(join(root, file)))
        shutil.copyfile(join(root, file), join(folder, file))  # 从本机拷贝文件到目标文件夹
        print("-----[复制完毕]%s------\n" % file)
        if getsize(join(root, file)) == getsize(join(folder, file)):  # 如果两边文件一样大小
            os.remove(join(root, file))  # 删除本地备份文件
            with open(logg_Text, "a+") as logg:  # 写进日志
                logg.write(("%s %s %s 复制成功[%s]\n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), root, file, getsize(join(folder, file)))))
            return
        else:  # 如果不一样大小
            os.remove(join(folder, file))  # 删除目标文件夹下的文件
            with open(logg_Text, "a+") as logg:  # 日志标记
                logg.write(("\n--***%s没有复制成功***--\n" % join(root, file)))
            return self.testFileSccess(root, file, folder)  # 重新执行本函数

    def clear_Up(self):  # 如果是周备，执行完后，新建文件夹，把对应的备份放进去
        for root, dirs, files in os.walk(self.y):  # 遍历当日文件夹
            for filename in files:
                folderName = filename.split("_backup_")[0]  # 取文件名的头
                filePath = join(self.y, folderName)  # 定义路径
                if not filePath:  # 如果没有这个文件夹
                    os.mkdir(filePath)  # 新建
                    shutil.copyfile(join(root, filename), join(filePath, filename))  # 拷贝
                else:
                    shutil.copyfile(join(root, filename), join(filePath, filename))  # 如果有就直接拷贝

    def log_doc(self):  # 结果对比写到日志文件
        if os.path.exists(self.y):
            with open(self.log, "a+") as logg:
                logg.write(("总数据：【{}】 from：{}\n总数据：【{}】 from：{}\n".format(self.sou, data_Back_Folder, self.getFileSize(self.y),
                                                                          y_File)))
            if not os.path.exists(join(y_File, "log.txt")):
                shutil.copyfile(self.log, join(y_File, "log.txt"))
                os.remove(self.log)

        if os.path.exists(self.x):
            with open(self.log, "a+") as logg:
                logg.write(("总数据：【{}】 from：{}\n总数据：【{}】 from：{}\n".format(self.sou, data_Back_Folder, self.getFileSize(self.x),
                                                                          x_File)))
            if not os.path.exists(join(x_File, "log.txt")):
                shutil.copyfile(self.log, join(x_File, "log.txt"))
                os.remove(self.log)

    def getFileSize(self, filename):  # 检查文件是否拷贝完整
        file_Dirc = {}
        lis = []
        for root, dirs, files in os.walk(filename):  # walk是遍历文件夹及子文件夹所有的文件
            for name in files:
                file_Dirc[join(root, name)] = getsize(join(root, name))
                lis.append(getsize(join(root, name)))
        return sum(lis)

if __name__ == '__main__':
    '''
    创建备份文件夹的路径
    创建日志路径
    格式化时间
    命名当日文件名
    定义备份路径
    '''
    data_Back_Folder = "E:\\n_bak"
    logg_Text = "E:\\log.txt"
    a, b, c, d, e, f, g, *h = time.localtime(time.time())
    new_Filename = "_".join([str(a), str(b), str(c)])
    x_File = "x:\\" + new_Filename  # 日备份
    y_File = "y:\\" + new_Filename  # 周备份
    # 实例化
    work_start = data_Maker_Work(x_File, y_File, data_Back_Folder, logg_Text)