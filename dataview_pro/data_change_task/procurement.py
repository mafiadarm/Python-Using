"""
以下为表的标准格式，变量可以更改
mysql_sentence， sql_sentence是必要信息
"""


class ConnectPackage:  # 按实际新建类去对应数据表
    # 日期
    date = "TB008"
    # 品名
    article = "TB038"
    # 品号
    number = "TB037"
    # 规格
    size = "TB039"
    # 单位
    unit = "TB040"
    # 数量
    amount = "TB019"
    # 单价
    price = "TB020"
    # 金额
    total_price = "TB009"


# 从这个数据库获取信息
cp = ConnectPackage()
data_table = "ROSUNDB.dbo.ACPTB"
# 必须要配合model里面的字段
data_fields = [
    cp.date, cp.article, cp.number, cp.size, cp.unit, cp.amount, cp.price, cp.total_price,
]

# 对应装数据的信息配置，要对应model里面的字段
mysql_sentence = r"""INSERT INTO production_procurementinfo (pro_date, article, art_num, art_size, unit, amount, price, total_price) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');"""

sql_sentence = "SELECT " + ",".join(data_fields) + " FROM " + data_table + " WHERE " + cp.date + " > "
