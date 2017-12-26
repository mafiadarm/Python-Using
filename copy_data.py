# _*_ coding:utf-8 _*_

'''
每次数据做了备份以后，要移到储存服务器
复制后，检查两边文件大小是否一致

检查文件夹是否为空
检查文件（夹）路径是否为真
检查日志文件是否存在
'''


import time, shutil, os
from os.path import join, getsize

def getFileSize(filename):  # 检查文件是否拷贝完整
    file_Dirc = {}
    lis = []
    for root, dirs, files in os.walk(filename):  # wolk是遍历文件夹及子文件夹所有的文件
        for name in files:
            file_Dirc[join(root, name)] = getsize(join(root, name))
            lis.append(getsize(join(root, name)))
    return sum(lis)

def testFileSccess(path, file, folder, logg_Text):
    shutil.copyfile(join(path, file), join(folder, file))
    if getsize(join(path, file)) == getsize(join(folder, file)):
        with open(logg_Text,"a+") as logg:
            logg.write(("%s %s %s 复制成功\n"%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),path,file)))
        os.remove(join(path, file))
    else:
        with open(logg_Text,"a+") as logg:
            logg.write(("\n--***%s没有复制成功***--\n"%join(path, file)))
        os.remove(join(folder, file))
        return testFileSccess(path, file, folder)

def DataBack(folder, data_Back_Folder, logg_Text):
    if not os.path.exists(folder):
        os.mkdir(folder)

    for root, dirs, files in os.walk(data_Back_Folder):
        if files:
            for file in files:
                testFileSccess(root, file, folder, logg_Text)
        else:
            print("%s下没有文件" % root)

def plan(x_File, y_File, data_Back_Folder):
    if 1< d <24:
        for root, dirs, files in os.walk(data_Back_Folder):
            if files:
                DataBack(x_File, data_Back_Folder, logg_Text)

    if g == 5 and 3< d <5:
        for root, dirs, files in os.walk(data_Back_Folder):
            if files:
                DataBack(y_File, data_Back_Folder, logg_Text)
        clearUp(y_File)

def clear_Up(y_File):
    for root, dirs, files in os.walk(y_File):
        for filename in files:
            folderName = fileName.split("_backup_")[0]
            filePath = join(y_File, folderName)
            if not filePath:
                os.mkdir(filePath)
                shutil.copyfile(join(root, filename), join(filePath, filename))
            else:
                shutil.copyfile(join(root, filename), join(filePath, filename))

def logg(sour_Data, x_File, y_File, data_Back_Folder, logg_Text):
    if os.path.exists(y_File):
        with open(logg_Text,"a+") as logg:
            logg.write(("总数据：【{}】 from：{}\n总数据：【{}】 from：{}\n".format(sour_Data, data_Back_Folder, getFileSize(y_File), y_File)))
        if not os.path.exists(join(x_File, "log.txt")):
            shutil.copyfile(logg_Text, join(y_File, "log.txt"))
            os.remove(logg_Text)
            
    if os.path.exists(x_File):
        with open(logg_Text,"a+") as logg:
            logg.write(("总数据：【{}】 from：{}\n总数据：【{}】 from：{}\n".format(sour_Data, data_Back_Folder, getFileSize(x_File), x_File)))
        if not os.path.exists(join(y_File, "log.txt")):
            shutil.copyfile(logg_Text, join(x_File, "log.txt"))
            os.remove(logg_Text)

if __name__ == '__main__':
    data_Back_Folder = "E:\\n_bak"
    logg_Text = "E:\log.txt"
    a, b, c, d, e, f, g, *h = time.localtime(time.time())
    new_Filename = "_".join([str(a), str(b), str(c)])
    x_File = "x:\\" + new_Filename  # 日备份
    y_File = "y:\\" + new_Filename  # 周备份
    sour_Data = getFileSize(dataBakcFolder)
    
    plan(x_File, y_File, data_Back_Folder)
    
    logg(sour_Data, x_File, y_File, data_Back_Folder, logg_Text)

    
