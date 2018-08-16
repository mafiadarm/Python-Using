"""
以下为表的标准格式，变量可以更改
mysql_sentence， sql_sentence是必要信息
"""


class ConnectPackage:  # 按实际新建类去对应数据表
    # 编号
    bill_number = "LE001"
    # 年
    close_year = "LE002"
    # 月
    close_month = "LE003"
    # 币种
    currency = "LE004"
    # 来源码
    source_bill = "LE005"
    # 部门
    department = "LE008"
    # 本币(借)
    domestic_currency_borrow = "LE014"
    # 本币(贷)
    domestic_currency_loan = "LE017"
    # 未过账(借)
    uncleared_borrow = "LE021"
    # 未过账(贷)
    uncleared_loan = "LE024"


# 从这个数据库获取信息
cp = ConnectPackage()
data_table = "ROSUNDB.dbo.ACTLE"
# 必须要配合model里面的字段
data_fields = [
    cp.bill_number, cp.close_year, cp.close_month, cp.currency,
    cp.source_bill, cp.department, cp.domestic_currency_borrow, cp.domestic_currency_loan,
    cp.uncleared_borrow, cp.uncleared_loan
]

# 对应装数据的信息配置，要对应model里面的字段
mysql_sentence = r"""INSERT INTO finance_balanceinfo (bill_number, close_year, close_month, currency, source_bill, department, domestic_currency_borrow, domestic_currency_loan, uncleared_borrow, uncleared_loan) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"""

sql_sentence = "SELECT " + ",".join(data_fields) + " FROM " + data_table
