"""
以下为表的标准格式，变量可以更改
mysql_sentence， sql_sentence是必要信息
"""


class ConnectPackage:  # 按实际新建类去对应数据表
    # 编号
    depart_number = "ME001"
    # 名称
    depart_name = "ME002"


# 从这个数据库获取信息
cp = ConnectPackage()
data_table = "ROSUNDB.dbo.CMSME"
# 必须要配合model里面的字段
data_fields = [
    cp.depart_number, cp.depart_name
]

# 对应装数据的信息配置，要对应model里面的字段
mysql_sentence = r"""INSERT INTO finance_departmentinfo (depart_number, depart_name) VALUES ('{}','{}');"""

sql_sentence = "SELECT " + ",".join(data_fields) + " FROM " + data_table
