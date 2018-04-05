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

import logging
import smtplib
import datetime

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


class Send:
    def __init__(self):
        self.smtp_server = "smtp.rosun.com.cn"  # smtp服务器地址
        self.from_mail = ""  # 邮件账号
        self.from_name = "2018年-%02d月薪资构成" % (datetime.date.today().month-1)  # 发送者名称[可任意修改]
        self.mail_pwd = ""
        self.to_mail = ""
        self.testPasswd()
        # self.mail_pwd = "r0sun*953@143@"  # 登陆密码

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
        msg = msg.encode("gb2312")  # 在客户端读取邮件的时候，如果出现乱码，要选择utf-8的编码

        s = smtplib.SMTP(self.smtp_server)
        s.login(self.from_mail, self.mail_pwd)
        s.sendmail(self.from_mail, to_mail, msg)
        s.quit()

    def testPasswd(self):
        while True:
            self.from_mail = input("请输入邮箱账号：")
            self.mail_pwd = input("请输入邮箱密码：")
            s = smtplib.SMTP(self.smtp_server)
            try:
                s.login(self.from_mail, self.mail_pwd)
                s.quit()
                break
            except Exception:
                print("密码错误！")


if __name__ == '__main__':
    se = Send()
