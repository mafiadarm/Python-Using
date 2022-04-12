import re
import os
import time
import requests
import json
import logging
import datetime
from multiprocessing.dummy import Pool

# 定义日志系统
logfile = str(datetime.date.today()) + '.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=logfile, level=logging.INFO, format=LOG_FORMAT)


def room_ids(page_count):
    rex = r'"rid":(.*?),'
    for i in range(1, page_count+1):
        url_head = f'https://www.douyu.com/gapi/rkc/directory/0_0/{i}'
        t_res = requests.get(url_head, headers=header)
        yield re.findall(rex, t_res.text)
    
    
def save(content):
    """保存指定内容"""
    with open('douyu_topic.txt', 'a+') as ww:
        ww.write(f'{content}\n')

def save_new(content):
    """保存指定内容"""
    with open('douyu_topic_new.txt', 'a+') as ww:
        ww.write(f'{content}\n')        

def save_lines(file_name, content):
    """保存指定内容到指定文件"""
    with open(file_name, 'w') as ww:
        ww.writelines(content)

        
def load(file_name):
    """读取指定文件内容"""
    with open(file_name, 'r+') as rr:
        content = rr.readlines()
    return [i.replace("\n", "") for i in content]


def douyu_url():
    """整理&拼接URL"""
    uu = read_room()
    dy_url_list = [f'https://www.douyu.com/topic/{k}?rid={rid}' for k, v in uu.items() for rid in v]
    return dy_url_list

        
def update(rid):
    """根据ID更新数据"""
    rex = r'window.zhtName="(.*?)",window.room_ids=\[(".*?")\],'
    rid_url = f'https://www.douyu.com/{rid}'
    r_res = requests.get(rid_url, headers=header)
    logging.info(f'开始测试 {rid}')
    title_rooms = re.findall(rex, r_res.text)
    if title_rooms:
        url_info = f'https://www.douyu.com/topic/{title_rooms[0][0]}?rid={rid}'
        logging.info(f'已获取到 {url_info}')
        print(f'已获取到 {url_info}')
        save(title_rooms[0][0])  # 只记录k

        
def compare():
    """比较两个文件的内容"""
    new = load('douyu_topic.txt')
    old = load('douyu_topic_old.txt')
    ing = set(new) ^ set(old)
    
    if not ing:
        print('no room close')
        print('no room open')
        return
    
    close = set(old) & ing
    if close:
        for c in close:
            print(f'close: {"https://douyu.com/topic/" + c}')
            logging.info(f'close: {"https://douyu.com/topic/" + c}')

    else:
        print('no room close')
              
    open_ = set(new) & ing
    if open_:
        for o in open_:
            print(f'open: {"https://douyu.com/topic/" + o}')
            logging.info(f'open: {"https://douyu.com/topic/" + o}')
            log_new = f'{str(datetime.date.today())} open: {"https://douyu.com/topic/" + o}'
            save_new(log_new)
    else:
        print('no room open')

    _n = '\n'.join(list(set(new)))
    save_lines('douyu_topic_old.txt', _n)  # 新的写入老的
    save_lines('douyu_topic.txt', '')   # 老的清空
    

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

time_loop = input('设置间隔时间(秒): ')
try:
    time_loop = int(time_loop)
except:
    print('设置的非数字，自动调整成8小时')
    time_loop = 8 * 60 * 60

# 循环
while 1:
    # 获取主站翻页数
    main_web = 'https://www.douyu.com/directory/all'
    web_res = requests.get(main_web, headers=header)

    rex = r'"pageCount":(\d+),'
    page_count = int(re.findall(rex, web_res.text)[0])        
     
    # 检查&新建需要使用的文件    
    if not os.path.exists('douyu_topic_old.txt'):
        with open('douyu_topic_old.txt', 'w') as ww_init:
            ww_init.write('')
            
    if not os.path.exists('douyu_topic.txt'):
        with open('douyu_topic.txt', 'w') as ww_init:
            ww_init.write('')

    if not os.path.exists('douyu_topic_new.txt'):
        with open('douyu_topic.txt', 'w') as ww_init:
            ww_init.write('')              
            

    pool = Pool(16)  # 16条并行线路
    for index, rids in enumerate(room_ids(page_count), 1):
        logging.info(f'------------开始扫描第 {index}/{page_count} 页------------')
        for rid in rids:
            pool.apply_async(update, (rid,))
            
    pool.close()
    pool.join()

    compare()

    time.sleep(time_loop)
