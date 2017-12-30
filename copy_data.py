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
        self.log = logg_text
        self.SourceFolder = from_source_folder
        self.TargetFolder = target_folder
        self.file_names = [join(path, file) for path, _, files in os.walk(self.SourceFolder) for file in files]

        self.ready_copy()
        self.check_folder()

    def ready_copy(self):
        print("\n-*- For Ready Copy to %s -*-\n" % self.TargetFolder)
        for source_file_name in self.file_names:
            self.doing_copy(source_file_name)

    def doing_copy(self, source_file_name):
        print("-*- Start Copy File [%s] -*-\n" % source_file_name)
        target_file_name = source_file_name.replace(self.SourceFolder, self.TargetFolder)
        target_path = os.path.split(source_file_name)[0].replace(self.SourceFolder, self.TargetFolder)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        shutil.copyfile(source_file_name, target_file_name)
        if getsize(source_file_name) == getsize(target_file_name):
            print("-*- Already Copy and Success -*-\n")
            with open(self.log, "a+") as logg:
                logg.write(("[{}] Already Copy From {}\n".format(getsize(source_file_name), source_file_name)))
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
            print("-*- Delete Source Files -*-\n")
            for delete_file in source_folder_files:
                os.remove(delete_file)
        else:
            if os.path.exists(join(self.TargetFolder, "log.txt")):
                print("\n-*- Delete Redundant Log File -*-\n")
                os.remove(join(self.TargetFolder, "log.txt"))
            print("-*- Some Files Without Copy -*-\n")
            difference = list(set(source_folder_files) - set(self.file_names))
            print("-*- %s Files in Plan -*-\n" % len(difference))
            for source_file_name in difference:
                self.doing_copy(source_file_name)
            self.check_folder()

    def log_write(self, source_folder_size, target_folder_size):
        notice = ("[{}] from：{}\n[{}] from：{}\n".format(source_folder_size, self.SourceFolder, target_folder_size, self.TargetFolder))
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
        folder_name = "{}_{}_{}_{}{}{}".format(a, b, c, "%02.f"%d, "%02.f"%e, "%02.f"%f)
        target_folder_x = "x:\\" + folder_name
        target_folder_y = "y:\\" + folder_name
        source_size = sum([getsize(join(path, file)) for path, _, files in os.walk(source_folder) for file in files])
        if d == 2 and source_size:
            start_copy = CopyWork(logg_Text, source_folder, target_folder_x)
        elif d == 5 and g == 5 and source_size:
            start_copy = CopyWork(logg_Text, source_folder, target_folder_y)
        time.sleep(1800)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
