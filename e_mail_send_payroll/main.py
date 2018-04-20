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
from collections import OrderedDict
from ready_email import *
from stuff import *

__author__ = 'Loffew'


class SendEmail(Send, Stuff):
    def __init__(self):
        super(Send, self).__init__()
        super(SendEmail, self).__init__()
        super(Stuff, self).__init__()
        self.get_email_addr()  # 获取员工信息里面的 工号：邮件
        self.filepath = "工资条.xlsx"  # 复制工资条文件路径到这里
        if not os.path.exists(self.filepath):
            input("当前文件夹没有《工资条.xlsx》,按回车键退出")
            quit()

    def readFileToSend(self):
        data = xlrd.open_workbook(self.filepath)
        table = data.sheet_by_index(0)  # 读取第一页所有数据
        rows = table.nrows
        object_name = OrderedDict({
            "部门": 0,
            "姓名": 2,
            "编号": 4,
            "基本工资": 5,
            "岗位工资": 6,
            "保密费": 7,
            "特区补贴": 8,
            "工龄工资": 9,
            "通信补贴": 10,
            "上月绩效": 11,
            "餐补": 12,
            "特殊岗位、室内交通、租房补贴": 13,
            "福利费": 14,
            "上月提成或计件": 15,
            "搬运": 16,
            "业绩超额奖金": 17,
            "其他": 18,
            "考核增加项": 26,
            "考核减少项": 42,
            "应发合计": 43,
            "代扣代缴社保": 47,
            "代扣代缴住房公积金": 48,
            "代扣代缴个人所得税": 49,
            "扣款": 50,
            "小计": 51,
            "补发已发": 52,
            "实发工资": 53,
            "发放渠道": 54,
            "公司承担社保": 55,
            "公司承担公积金": 56,
        })

        for row in range(4, rows):
            # time.sleep(1)
            values = table.row_values(row)
            if not values[4]: continue
            if values[4] in self.already:
                print("%s 已发送" % values[4])
                continue

            get_list = []

            for name, num in object_name.items():
                get_list.append(name + "一" * (20 - len(name)) + str(values[num]) + "\n")

            body = "".join(get_list)

            mail = self.stuff_info.get(values[4])

            if mail:
                try:
                    self.to_mail = mail
                    self.send(body)
                    print(values[1], values[2], "邮件已发送")

                    with open("already_send.txt", "a") as aa:
                        aa.write("%s\n" % values[4])

                except Exception as ex:
                    print("%s error, please check error.txt!" % values[4])
                    with open("no_email.txt", "a", encoding="utf8") as rr:
                        rr.write("%s %s %s 未发送邮件\n" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), values[4], values[2]))
                    with open("error.txt", "a", encoding="utf8") as ee:
                        ee.write("%s %s\n" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ex))
            else:
                print("%s %s 没有邮箱，未发送邮件，请检查 员工信息.xlsx" % (values[1], values[2]))
                with open("no_email.txt", "a", encoding="utf8") as rr:
                    rr.write("%s %s %s 未发送邮件，请检查 员工信息.xlsx\n" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), values[4], values[2]))


if __name__ == '__main__':
    s = SendEmail()
    s.readFileToSend()
    s.s.quit()
    input("执行完毕！按回车结束！")



