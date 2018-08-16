"""
以下为表的标准格式，变量可以更改
mysql_sentence， sql_sentence是必要信息
"""
"""
视图样式:
SELECT     MOCTA.TA001 AS MOCTATA001, MOCTA.TA002 AS MOCTATA002, MOCTA.TA006 AS MOCTATA006, MOCTA.TA034 AS MOCTATA034, MOCTA.TA007 AS MOCTATA007, 
                      MOCTA.TA035 AS MOCTATA035, MOCTA.TA009 AS MOCTATA009, MOCTA.TA010 AS MOCTATA010, MOCTA.TA014 AS MOCTATA014, MOCTA.TA011 AS MOCTATA011, 
                      MOCTA.TA057 AS MOCTATA057, MOCTG.TG011 AS MOCTGTG011
FROM         dbo.MOCTA AS MOCTA LEFT OUTER JOIN
                      dbo.MOCTG AS MOCTG ON MOCTG.TG014 = MOCTA.TA001 AND MOCTG.TG015 = MOCTA.TA002
WHERE     (MOCTA.TA013 <> 'V')
"""

class ConnectPackage:  # 按实际新建类去对应数据表
    # 单别
    order_type = "MOCTATA001"
    # 单号
    order_number = "MOCTATA002"
    # 品名
    pro_name = "MOCTATA006"
    # 品号
    pro_num = "MOCTATA034"
    # 单位
    unit = "MOCTATA007"
    # 规格
    p_size = "MOCTATA035"
    # 预计开工
    plan_start = "MOCTATA009"
    # 预计完工
    plan_end = "MOCTATA010"
    # 实际完工
    reality_time = "MOCTATA014"
    # 状态码
    stat_code = "MOCTATA011"
    # 批号
    batch = "MOCTATA057"
    # 入库数量
    into_count = "MOCTGTG011"


# 从这个数据库获取信息
cp = ConnectPackage()
data_table = "ROSUNDB.dbo.SCKB"
# 必须要配合model里面的字段
data_fields = [
    cp.order_type, cp.order_number, cp.pro_name, cp.pro_num, cp.unit, cp.p_size, cp.plan_start, cp.plan_end, cp.reality_time, cp.stat_code, cp.batch, cp.into_count
]

# 对应装数据的信息配置，要对应model里面的字段
mysql_sentence = r"""INSERT INTO repertory_orderstat (order_type, order_number, pro_num, pro_name, unit, p_size, plan_start, plan_end, reality_time, stat_code, batch, into_count) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"""

sql_sentence = "SELECT TOP 50 * " + " FROM " + data_table + " ORDER BY " + '"MOCTATA002"' + " DESC"
