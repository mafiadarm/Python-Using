# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_24_2018  9:38
   File Name:      /GitHub/ListeRaid
   Creat From:     PyCharm
   Python version:  2.7
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

__author__ = 'Loffew'

import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


# rpm2cpio MegaCli-8.07.14-1.noarch.rpm | cpio -dimv
'''
root@salt-minion2:~#sudo ./opt/MegaRAID/MegaCli/MegaCli64 -AdpAllInfo -aAll

Adapter #0

==============================================================================
                    Versions
                ================
Product Name    : PERC H700 Adapter
Serial No       : 1C601NX
FW Package Build: 12.10.1-0001

                    Mfg. Data
                ================
Mfg. Date       : 12/07/11
Rework Date     : 12/07/11
Revision No     : A05
Battery FRU     : N/A

                Image Versions in Flash:
                ================
BIOS Version       : 3.18.00_4.09.05.00_0x0416A000
FW Version         : 2.100.03-1062
Preboot CLI Version: 04.04-010:#%00008
Ctrl-R Version     : 2.02-0025
NVDATA Version     : 2.07.03-0003
Boot Block Version : 2.02.00.00-0000
BOOT Version       : 01.250.04.219

                Pending Images in Flash
                ================
None
......
'''

# MegaCli64 -AdpAllInfo -aAll  #查看RAID卡信息
#
# MegaCli64 -PDList -aALL   #查看硬盘信息
'''
root@zhi:~# ./opt/MegaRAID/MegaCli/MegaCli64 -AdpAllInfo -aAll

Adapter #0

==============================================================================
                    Versions
                ================
Product Name    : PERC H700 Adapter
Serial No       : 1C601NX
FW Package Build: 12.10.1-0001

...

                Device Present
                ================
Virtual Drives    : 3 
  Degraded        : 0 
  Offline         : 0 
Physical Devices  : 4 
  Disks           : 3 
  Critical Disks  : 0 
  Failed Disks    : 0 

...


root@zhi:~# ./opt/MegaRAID/MegaCli/MegaCli64 -PDList -aALL                                     

Adapter #0

Enclosure Device ID: 32
Slot Number: 0
Drives position: DiskGroup: 0, Span: 0, Arm: 0
Enclosure position: N/A
Device Id: 0
WWN: 5000C5001D5F0CA0
Sequence Number: 2
Media Error Count: 0     #代表扇区有问题，坏道等,数值越大越严重。
Other Error Count: 0     #代表磁盘可能有松动
Predictive Failure Count: 0
Last Predictive Failure Event Seq Number: 0
PD Type: SAS
'''

# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------
#    Filename:
#      Author: zhi
#        Mail: 937042882@qq.com
#     Version: 0.0.1
#  LastChange:
# ---------------------------------------------

import re
import subprocess


def read_raid_info():
    try:
        allInfo = subprocess.check_output(['/root/MegaRAID/MegaCli/MegaCli64', '-AdpAllInfo', '-aALL'])
    except OSError as e:
        return None
    return (i for i in allInfo.split('\n\n') if i)


def get_raid_info(info):
    detail_info = {}
    version = re.compile(r'Versions')
    name = re.compile(r'Product Name')
    device = re.compile(r'Device Present')
    colon = re.compile(r':')
    for i in info:
        if version.search(i):
            for eachLine in i.split('\n'):
                if name.search(eachLine):
                    detail_info['Product Name'] = eachLine.split(':')[1].strip()
        if device.search(i):
            for eachLine in i.split('\n'):
                if colon.search(eachLine):
                    detail_info[eachLine.split(':')[0].strip()] = eachLine.split(':')[1].strip()
    return detail_info


def read_disk_info():
    try:
        allInfo = subprocess.check_output(['/root/MegaRAID/MegaCli/MegaCli64', '-PDList', '-aALL'])
    except OSError as e:
        return None
    return (i for i in allInfo.split('\n') if i)


def get_disk_info(info):
    media = re.compile(r'Media Error Count')
    other = re.compile(r'Other Error Count')
    media_count = 0
    other_count = 0
    for i in info:
        if media.match(i):
            if i.split(':')[1].strip() != '0':
                media_count += 1
        if other.match(i):
            if i.split(':')[1].strip() != '0':
                other_count += 1
    detail_info = {'MediaErrorCount': str(media_count), 'OtherErrorCount': str(other_count)}
    return detail_info


def main():
    all_info = {}
    raid_info = read_raid_info()
    disk_info = read_disk_info()
    if raid_info:
        all_info.update(get_raid_info(raid_info))
    else:
        print('No megacli client.')
        return None
    if disk_info:
        all_info.update(get_raid_info(disk_info))
    return all_info
