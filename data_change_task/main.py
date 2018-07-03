import decimal

from from_sqlserver_to_mysql import *
import sellproxy


def main(*args):
    # sqlserver登陆信息
    info = MakeDatabaseInfo()
    info.basePT = "/home/zzz/Documents"
    info.getInfo()

    # mysql登陆信息
    mysql_data_info = {
        "host": "localhost",
        "username": "root",
        "password": "1",
        "database": "rosun_sell"  # rosun_data
    }

    try:
        sql_connect = SqlConnect(info.BASE_DB)
        mysql_connect = MysqlUse(**mysql_data_info)

        for sentence in args:
            mysql_sentence, sql_sentence = sentence

            # block 为了日期不重复
            datatable = mysql_sentence.split()[2]  # 获取要插入的表名
            daysql = "select * from {} order by id desc limit 1;".format(datatable)  # 查询最后一条语句，获取日期
            mysql_connect.executeSql(daysql)
            results = mysql_connect.cur.fetchall()  # 返回tuple

            if not len(results):  # 判度数据是否为空，为空则从头开始查询
                date = "20141231"
            else:
                date = str("".join(str(results[0][1]).split("-")))
            # endclock

            # 提取sqlserver
            data = sql_connect.query_data(sql_sentence + date)  # list格式

            # 导入mysql
            for d in data:
                n = [str(x) if str(x).isdigit() or isinstance(x, decimal.Decimal) else str(x.strip()) for x in d]
                n[0] = str(f"{n[0][:4]}-{n[0][4:6]}-{n[0][6:8]}")  # 对日期单独处理

                mysql_connect.executeSql(mysql_sentence.format(*n))

        # 执行事物
        mysql_connect.conn.commit()

    except Exception as Ex:
        print(Ex)
    finally:
        # 关闭数据库
        sql_connect.close()
        mysql_connect.connClose()


if __name__ == '__main__':
    # 在这里增加数据库导入文件的交换语句变量，元组包裹，注意顺序
    sentence_list = [
        (sellproxy.mysql_sentence, sellproxy.sql_sentence),
    ]

    main(*sentence_list)
