import decimal
from tqdm import tqdm

import time

import datetime

from from_sqlserver_to_mysql import *
import sellproxy
import selldirect  # 增加文件导入
import procurement


def timestamp(t):
    timearray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timearray))


def sleep_second():
    target = "{} 23:59:00".format(str(datetime.date.today()))[:19]
    now = str(datetime.datetime.now())[:19]

    diff = timestamp(target) - timestamp(now)

    print("The next copy at next 23:59:00\nPROCESS:")
    time.sleep(0.01)
    [time.sleep(1) for _ in tqdm(range(diff))]


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
        mysql_connect = MysqlUse(**mysql_data_info)

        return mysql_connect, sql_connect

    except Exception as Ex:
        print(Ex)


def main(database_name, *args):
    print("开始执行程序...")
    mysql, sqlserver = connect_database(database_name)  # 启动新的连接
    print("数据库连接成功...")

    for sentence in args:
        mysql_sentence, sql_sentence, sql_table = sentence
        print("获得取行语句...")

        # block 为了日期不重复
        datatable = mysql_sentence.split()[2]  # 获取要插入的表名
        print("执行表名为：", datatable)
        # daysql = "select * from {} order by id desc limit 1;".format(datatable)  # 查询最后一条语句，获取日期
        # count_mysql = "select count(*) from {}".format(datatable)
        # mysql.executeSql(count_mysql)
        # results = mysql.cur.fetchone() # 返回tuple (11437,)

        # if not results[0]:  # 判度数据是否为空，为空则从头开始查询
        # else:  # 如果不为空，则导入增量[源数据库如果有删除动作，此处手动删除mysql的表内容重新导入] 使用truncate tablename
        mysql.executeSql("truncate {}".format(datatable))  # 视图制作缺id不能导增量
        print("删除历史数据")
        # 提取sqlserver
        date = "20141231"  # 从此日期开始
        print("获取源数据")
        data = sqlserver.query_data(sql_sentence + date)  # list格式, 获取大于最后日期的

        # endclock

        # 导入mysql
        print("开始导入数据到mysql...")
        for d in data:
            n = [str(x) if str(x).isdigit() or isinstance(x, decimal.Decimal) else str(x.strip()).replace("'", "") for x
                 in d]
            n[0] = str(f"{n[0][:4]}-{n[0][4:6]}-{n[0][6:8]}")  # 对日期单独处理
            # print(n)
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


if __name__ == '__main__':
    # 在这里增加数据库导入文件的交换语句变量，元组包裹，mysql在前，sqlserver在后
    sentence_list = [
        (sellproxy.mysql_sentence, sellproxy.sql_sentence, sellproxy.data_table),  # 增加语句引用
        (selldirect.mysql_sentence, selldirect.sql_sentence, selldirect.data_table),
        (procurement.mysql_sentence, procurement.sql_sentence, procurement.data_table),
    ]

    while True:
        main("rosun", *sentence_list)
        sleep_second()
