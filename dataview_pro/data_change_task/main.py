import decimal
import time
import datetime
from multiprocessing import Process
from tqdm import tqdm

import data_sellproxy
import data_selldirect  # 增加文件导入
import data_procurement
import data_finance
import data_department
import data_production_order
from from_sqlserver_to_mysql import *


def timestamp(t):
    timearray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timearray))


def sleep_one(count):
    [time.sleep(1) for _ in tqdm(range(count))]


def sleep_second(_):
    target = "{} 23:59:59".format(str(datetime.date.today())[:19])
    now = str(datetime.datetime.now())[:19]

    diff = timestamp(target) - timestamp(now)

    print("The next copy at next 23:59:59\nPROCESS:")

    [time.sleep(1) for _ in tqdm(range(diff))]

    time.sleep(1)


def connect_database(database):
    # sqlserver登陆信息
    info = MakeDatabaseInfo()
    info.basePT = "/home/zzz/Documents"
    info.getInfo()

    # mysql登陆信息
    mysql_data_info = {
        "host": "localhost",
        "username": "root",
        "password": "1",
        "database": database
    }

    try:
        sql_connect = SqlConnect(info.BASE_DB)
        print("SQLSERVER CONNECT!")
    except Exception as Ex:
        print("PLEASE CHECK CONNECT INFORMATION OF SQLSERVER", Ex)

    try:
        mysql_connect = MysqlUse(**mysql_data_info)
        print("MYSQL CONNECT!")
    except Exception as Ex:
        print("PLEASE CHECK CONNECT INFORMATION OF MYSQL", Ex)
    
    if mysql_connect and sql_connect:
        print("get mysql_connect and sql_connect!")
        return mysql_connect, sql_connect
    else:
        print("get again!")
        time.sleep(3)
        return connect_database(database)
        


def main(database_name, *args):
    print("开始执行程序...")
    mysql, sqlserver = connect_database(database_name)  # 启动新的连接
    print("数据库连接成功...")

    for sentence in args:
        mysql_sentence, sql_sentence, sql_table, flag = sentence
        print("获得取行语句...")

        # {
        # 为了日期不重复
        datatable = mysql_sentence.split()[2]  # 获取要插入的表名
        print("执行表名为：", datatable)
        # daysql = "select * from {} order by id desc limit 1;".format(datatable)  # 查询最后一条语句，获取日期
        # count_mysql = "select count(*) from {}".format(datatable)
        # mysql.executeSql(count_mysql)
        # results = mysql.cur.fetchone() # 返回tuple (11437,)

        # if not results[0]:  # 判度数据是否为空，为空则从头开始查询
        # else:  # 如果不为空，则导入增量[源数据库如果有删除动作，此处手动删除mysql的表内容重新导入] 使用truncate tablename
        print("删除历史数据")
        mysql.executeSql("truncate {}".format(datatable))  # 视图制作缺id不能导增量

        # 提取sqlserver
        # "20141231"  # 默认从此日期开始
        print("获取源数据")
        data = sqlserver.query_data(sql_sentence)  # list格式, 获取大于最后日期的

        # }

        # 导入mysql
        print("开始导入数据到mysql...")
        for d in data:
            n = [str(x).replace("'", "") if str(x).isdigit() or isinstance(x, decimal.Decimal) or not None else str(x.strip()).replace("'", "") for x in d]
            if flag == 1:
                n[0] = str(f"{n[0][:4]}-{n[0][4:6]}-{n[0][6:8]}")  # 对日期单独处理
            # print(n)
            if flag == 3:
                if n[-1] == "None":
                    n[-1] = 0
            mysql.executeSql(mysql_sentence.format(*n))

        mysql.conn.commit()
        print("导入完毕！")

        mysql.executeSql("select count(*) from {}".format(datatable))
        print("mysql_{} 条数为:".format(datatable), mysql.cur.fetchone()[0])
        print("sql_{} 条数为:".format(datatable).format(sql_table), len(data))

    print("关闭数据库...")
    mysql.connClose()
    sqlserver.close()
    print("关闭数据库成功！")


def run(sen_list, time_control, count):
    """
    :param sen_list: 语句列表
    :param time_control: 时间控制方法
    :param count: 时间
    :return:
    """

    while True:
        main("rosun", *sen_list)
        time_control(count)


if __name__ == '__main__':

    # 在这里增加数据库导入文件的交换语句变量，元组包裹，mysql在前，sqlserver在后
    # 1 代表需要处理日期
    # 2 代表不需要单独处理
    sentence_list = [
        (data_sellproxy.mysql_sentence, data_sellproxy.sql_sentence, data_sellproxy.data_table, 1),  # 增加语句引用
        (data_selldirect.mysql_sentence, data_selldirect.sql_sentence, data_selldirect.data_table, 1),
        (data_procurement.mysql_sentence, data_procurement.sql_sentence, data_procurement.data_table, 1),
        (data_finance.mysql_sentence, data_finance.sql_sentence, data_finance.data_table, 2),
        (data_department.mysql_sentence, data_department.sql_sentence, data_department.data_table, 2),
    ]

    fast_list = [
        (data_production_order.mysql_sentence, data_production_order.sql_sentence, data_production_order.data_table, 3),
    ]

    p1 = Process(target=run, args=(sentence_list, sleep_second, 1))
    p2 = Process(target=run, args=(fast_list, sleep_one, 60*5))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
