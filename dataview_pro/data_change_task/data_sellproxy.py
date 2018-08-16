"""
以下为表的标准格式，变量可以更改
mysql_sentence， sql_sentence是必要信息
"""

class ConnectPackage:  # 按实际新建类去对应数据表
    date = "COPTGTG003"
    odd = "COPTHTH002"
    article = "COPTHTH005"
    number = "COPTHTH004"
    unit = "COPTHTH006"
    per_unit = "COPTHTH008"
    total_price = "COPTHTH013"
    add1 = "COPTCTC010"
    add2 = "COPTCTC011"
    province = "COPTCUDF02"
    dbt_agent = "COPTCUDF03"
    company = "COPMAMA002"


# 从这个数据库获取信息
cp = ConnectPackage()
data_table = "ROSUNDB.dbo.dl"
# 必须要配合model里面的字段
data_fields = [  # 年份 单号 品名 品号 单位 单价 总价 地址1 地址2 省份 代理商 公司
    cp.date, cp.odd, cp.article, cp.number,
    cp.unit, cp.per_unit,
    cp.total_price, cp.add1,
    cp.add2, cp.province,
    cp.dbt_agent, cp.company,
]

# 对应装数据的信息配置，要对应model里面的字段
mysql_sentence = r"""INSERT INTO sell_sellproxyinfo (sell_date, odd, article, art_num, unit, price, total_price, add1, add2, province, proxy, company) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"""

sql_sentence = "SELECT " + ",".join(data_fields) + " FROM " + data_table + " WHERE " + cp.date + " > 20141231"

