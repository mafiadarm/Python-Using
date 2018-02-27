#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_27_2018  11:49
   File Name:      /GitHub/payroll
   Creat From:     PyCharm
   Python version: 3.6.2  
- - - - - - - - - - - - - - - 
   Description:
   用邮件一次性让人资发送工资单
   人资是用excel储存工资单信息，通过用xlrd读取excel文件
        按行读取信息
        发送信息到当前行的邮件
==============================
"""

import logging
import xlrd
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

def formatAddr(mail):
    name, addr = parseaddr(mail)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(body_list):
    smtp_server = "smtp.rosun.com.cn"  # smtp服务器地址
    from_mail = "hq-it@rosun.com.cn"  # 邮件账号
    mail_pwd = "r0sun*953@143@"  # 登陆密码

    to_mail = ["zhongshuai@rosun.com.cn"]  # 接收邮件的地址
    from_name = "集团流程IT部"  # 发送者名称[可任意修改]
    subject = "工资表"  # 标题[可任意修改]
    # body_list.insert(0, "时间:" + str(datetime.date.today()))
    # body = "\n".join(body_list)

    # mail = [
    #     "From: %s <%s>" % (from_name, from_mail),
    #     "To: %s" % ','.join(to_mail),
    #     "Subject: %s" % subject,
    #     "",
    #     body
    # ]
    body = '''
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            * {
                margin: 0;
                padding: 0;
            }
             .clearfix:after{
                content: "";
                display: block;
                clear: both;
            }
            ul{
                margin: 1px auto;
                border: 5px solid yellow;
                width: 500px;
                /*overflow: hidden;*/
                /*height: 20px;*/
    
            }
            li{
                list-style: none;
                width: 100px;
                height: 100px;
                border: 1px solid red;
                float: left;
                /*float: right;*/
            }
        </style>
        </head>
    <body>
    <ul class="clearfix">
        <li style="width: 420px">特殊岗位补贴/外勤、市内交通、驻点租房补贴</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
    </ul>
        <ul class="clearfix">
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
    </ul>
    </body>
    
    '''  # 内容[用网页方式发送]

    msg = MIMEMultipart()  # 构造一个msg
    msg["From"] = formatAddr("{} <{}>".format(from_name, from_mail))
    msg["To"] = ','.join(to_mail)
    msg["Subject"] = "标题"
    msg.attach(MIMEText(body, 'html', 'utf-8'))

    # msg = '\n'.join(mail)
    # msg = msg.encode("gb2312")  # 在客户端读取邮件的时候，如果出现乱码，要选择utf-8的编码

    s = smtplib.SMTP(smtp_server)
    s.login(from_mail, mail_pwd)
    # s.sendmail(from_mail, to_mail, msg)
    s.sendmail(from_mail, to_mail, msg.as_string())
    s.quit()

if __name__ == '__main__':
    send_mail([1,2])
    # data = xlrd.open_workbook("C:/Users/lo/Desktop/test.xlsx")
    # table = data.sheet_by_name(u'Sheet1')
    # rows = table.nrows
    #
    # for row in range(1, rows):
    #     title = table.row_values(0)
    #     for index, rr in enumerate(table.row_values(row)):
    #         title[index] += ":" + str(rr)
    #     send_mail(title)
    #     print(title)
