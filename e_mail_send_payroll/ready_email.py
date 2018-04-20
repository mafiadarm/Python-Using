#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_26_2018  17:00
    File Name:      /Python-Using/send_email
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import smtplib
import datetime
from getpass import getpass

__author__ = 'Loffew'


class Send:
    def __init__(self):
        this_month = datetime.date.today().month - 1
        this_year = datetime.date.today().year
        if not this_month:
            this_month = 12
            this_year -= 1

        self.smtp_server = "smtp.rosun.com.cn"  # smtp服务器地址
        self.from_mail = ""  # 邮件账号
        self.from_name = "%02d年-%02d月薪资构成" % (this_year, this_month)  # 发送者名称[可任意修改]
        self.mail_pwd = ""
        self.to_mail = ""

        self.testPasswd()

    def send(self, body):
        to_mail = [self.to_mail]  # 接收邮件的地址

        subject = self.from_name  # 标题[可任意修改]

        mail = [
            "From: %s <%s>" % (self.from_name, self.from_mail),
            "To: %s" % ','.join(to_mail),
            "Subject: %s" % subject,
            "",
            body
        ]
        msg = '\n'.join(mail)
        # bossmail 默认为gb2312
        msg = msg.encode("utf-8")  # 在客户端读取邮件的时候，如果出现乱码，要选择utf-8的编码

        self.s.sendmail(self.from_mail, to_mail, msg)

    def testPasswd(self):
        while True:
            self.from_mail = input("请输入邮箱账号：")
            self.mail_pwd = getpass("请输入邮箱密码：")
            # self.mail_pwd = input("请输入邮箱密码：")

            self.s = smtplib.SMTP(self.smtp_server)
            try:
                self.s.login(self.from_mail, self.mail_pwd)
                break
            except Exception:
                print("密码错误！")


if __name__ == '__main__':
    se = Send()
