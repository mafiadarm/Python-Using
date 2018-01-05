import time
import shutil
import os
import datetime
from os.path import join, getsize
from multiprocessing.dummy import Pool


class CopyWork:
    def __init__(self, logg_text, from_source_folder, target_folder):
        self.log = logg_text
        self.SourceFolder = from_source_folder
        self.TargetFolder = target_folder
        self.file_names = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]
        self.log_messages = []

        self.put_files_in_pool(self.file_names)
        self.check_folder()
        pool.close()
        pool.join()

    def put_files_in_pool(self, file_names):
        folders = [os.path.split(path)[0].replace(self.SourceFolder, self.TargetFolder) for path in file_names]
        for folder in folders:
            pool.apply_async(self.make_folders, args=(folder,))
        for file in file_names:
            pool.apply_async(self.copy_file, args=(file, file.replace(self.SourceFolder, self.TargetFolder)))

    def make_folders(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
            self.log_messages.append("make folder %s\n" % folder)

    def copy_file(self, source_file_name, target_file_name):
        print("-*- start copy ", source_file_name, "to", target_file_name)
        shutil.copyfile(source_file_name, target_file_name)
        print("-*- success ", source_file_name)
        self.log_messages.append("[{}] Copy Successfully {}\n".format(getsize(source_file_name), target_file_name))

    def check_folder(self):
        print("-*- Check File of All -*-\n")
        source_folder_files = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]
        source_folder_size = sum([getsize(file) for file in source_folder_files])
        target_folder_files = [join(path, file) for path, _, files in os.walk(self.TargetFolder) for file in files]
        target_folder_size = sum([getsize(file) for file in target_folder_files])
        if source_folder_size == target_folder_size:
            print("-*- All of Files in %s and Start Write Log -*-\n" % self.TargetFolder)
            self.log_write(source_folder_size, target_folder_size)
            print("-*- Delete Source Files and Ending -*-\n")
            for delete_file in source_folder_files:
                os.remove(delete_file)
        else:
            print("-*- Some Files Without Copy -*-\n")
            difference = list(set(source_folder_files) - set(self.file_names))
            print("-*- %s Files in Plan -*-\n" % len(difference))
            self.put_files_in_pool(difference)
            self.check_folder()

    def log_write(self, source_folder_size, target_folder_size):
        self.log_messages.append("[{}] from：{}\n[{}] from：{}\n".format(source_folder_size, self.SourceFolder, target_folder_size, self.TargetFolder))
        with open(self.log, "a+") as logg:
            logg.writelines(self.log_messages)
        print("-*- Copy log.txt to %s -*-\n" % self.TargetFolder)
        self.make_folders(self.TargetFolder)
        shutil.copyfile(self.log, join(self.TargetFolder, "log.txt"))
        os.remove(self.log)

if __name__ == '__main__':
    print("Start From ", datetime.datetime.now().strftime("%c"))
    while True:
        pool = Pool()
        logg_Text = "E:\\log.txt"
        source_folder = "E:\\n_bak"
        a, b, c, d, e, f, g, *h = time.localtime(time.time())
        folder_name = "{}_{}_{}_{}{}{}".format(a, b, c, "%02.f" % d, "%02.f" % e, "%02.f" % f)
        target_folder_x = "x:\\" + folder_name
        target_folder_y = "y:\\" + folder_name
        source_size = sum([getsize(join(path, file)) for path, _, files in os.walk(source_folder) for file in files])
        if d == 2 and source_size:
            start_copy = CopyWork(logg_Text, source_folder, target_folder_x)
        elif d == 5 and g == 5 and source_size:
            start_copy = CopyWork(logg_Text, source_folder, target_folder_y)
        time.sleep(1800)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


