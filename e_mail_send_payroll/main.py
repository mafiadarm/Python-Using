#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_26_2018  17:15
    File Name:      /Python-Using/get_body
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    从工资表excel里面读取数据
==============================
"""

from ready_to_email import *
from stuff_email import *

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s", filename="log.txt")


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


class SendEmail(Send, Stuff):
    def __init__(self):
        super(Send, self).__init__()
        super(SendEmail, self).__init__()
        super(Stuff, self).__init__()
        self.get_email_addr()
        self.filepath = input("文件路径：")

    def readFileToSend(self):
        data = xlrd.open_workbook(self.filepath)
        table = data.sheet_by_index(0)
        rows = table.nrows

        object_name = [
            "部门",
            "姓名",
            "编号",
            "基本工资",
            "岗位工资",
            "保密费",
            "特区补贴",
            "工龄工资",
            "通信补贴",
            "上月绩效",
            "餐补",
            "特殊岗位、室内交通、租房补贴",
            "福利费",
            "上月提成",
            "搬运",
            "业绩超额奖金",
            "其他",
            "考核增加",
            "考核减少",
            "应发合计",
            "代缴社保",
            "代缴住房公积金",
            "代缴个人所得税",
            "扣款",
            "小计",
            "补发已发",
            "实发工资",
            "发放渠道",
            "公司承担社保",
            "公司承担公积金",
        ]

        for row in range(4, rows):
            get_list = []
            values = table.row_values(row)
            for name, value in zip(object_name, values):
                get_list.append(name + "一"*(20-len(name)) + str(value) + "\n")
            body = "".join(get_list)

            mail = self.stuff_info.get(values[2])

            if mail:
                self.to_mail = mail
                self.send(body)
                print(values[1], values[2], "邮件已发送")
            else:
                pp_dbg(*("%s %s 没有邮箱，未发送邮件，请检查 员工信息.xlsx" % (values[1], values[2])))


if __name__ == '__main__':
    s = SendEmail()
    s.readFileToSend()



