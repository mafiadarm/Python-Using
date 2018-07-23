#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_20_2018  14:33
    File Name:      /pychart_SqlServer/main
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    直营获取sql：
    SELECT     COPTG.TG003 AS COPTGTG003, COPTH.TH005 AS COPTHTH005, COPTH.TH006 AS COPTHTH006, COPTH.TH008 AS COPTHTH008, COPTH.TH013 AS COPTHTH013,
                      COPTC.TC010 AS COPTCTC010, COPTC.TC011 AS COPTCTC011, COPTC.UDF02 AS COPTCUDF02, COPMA.MA002 AS COPMAMA002, CMSME.ME002 AS CMSMEME002,
                      CMSMV.MV002 AS CMSMVMV002
    FROM       dbo.COPTG AS COPTG LEFT OUTER JOIN
                      dbo.COPTH AS COPTH ON COPTH.TH001 = COPTG.TG001 AND COPTH.TH002 = COPTG.TG002 LEFT OUTER JOIN
                      dbo.CMSMV AS CMSMV ON CMSMV.MV001 = COPTG.TG006 LEFT OUTER JOIN
                      dbo.CMSME AS CMSME ON CMSME.ME001 = COPTG.TG005 LEFT OUTER JOIN
                      dbo.COPTC AS COPTC ON COPTC.TC001 = COPTH.TH014 AND COPTC.TC002 = COPTH.TH015 LEFT OUTER JOIN
                      dbo.COPMA AS COPMA ON COPMA.MA001 = COPTC.TC004
    WHERE     (COPTG.TG001 = '2301') AND (COPTG.TG003 > '20150101') AND (COPTG.TG004 LIKE 'c%') AND (COPTH.TH002 > '20150101001') AND (COPTG.TG023 = 'Y') AND
                      (COPTH.TH020 = 'Y') AND (COPTH.TH001 = '2301') AND (COPTC.TC027 = 'Y') AND (COPTC.TC003 > '20150101') AND (COPTC.TC001 = '2220') AND
                      (COPTC.TC004 LIKE 'c%')
	直营更新
	SELECT     COPTG.TG003 AS COPTGTG003, COPTH.TH005 AS COPTHTH005, COPTH.TH006 AS COPTHTH006, COPTH.TH008 AS COPTHTH008, COPTH.TH013 AS COPTHTH013, 
                      COPTC.TC010 AS COPTCTC010, COPTC.TC011 AS COPTCTC011, COPTC.UDF02 AS COPTCUDF02, COPMA.MA002 AS COPMAMA002, CMSME.ME002 AS CMSMEME002, 
                      CMSMV.MV002 AS CMSMVMV002, COPTH.TH002 AS COPTHTH002, COPTH.TH004 AS COPTHTH004
	FROM         dbo.COPTG AS COPTG LEFT OUTER JOIN
                      dbo.COPTH AS COPTH ON COPTH.TH001 = COPTG.TG001 AND COPTH.TH002 = COPTG.TG002 LEFT OUTER JOIN
                      dbo.CMSMV AS CMSMV ON CMSMV.MV001 = COPTG.TG006 LEFT OUTER JOIN
                      dbo.CMSME AS CMSME ON CMSME.ME001 = COPTG.TG005 LEFT OUTER JOIN
                      dbo.COPTC AS COPTC ON COPTC.TC001 = COPTH.TH014 AND COPTC.TC002 = COPTH.TH015 LEFT OUTER JOIN
                      dbo.COPMA AS COPMA ON COPMA.MA001 = COPTC.TC004
	WHERE     (COPTG.TG001 = '2301') AND (COPTG.TG003 > '20150101') AND (COPTG.TG004 LIKE 'c%') AND (COPTH.TH002 > '20150101001') AND (COPTG.TG023 = 'Y') AND 
                      (COPTH.TH020 = 'Y') AND (COPTH.TH001 = '2301') AND (COPTC.TC027 = 'Y') AND (COPTC.TC003 > '20150101') AND (COPTC.TC001 = '2220') AND 
                      (COPTC.TC004 LIKE 'c%')

    代理获取sql：
    SELECT     COPTG.TG003 AS COPTGTG003, COPTH.TH005 AS COPTHTH005, COPTH.TH006 AS COPTHTH006, COPTH.TH008 AS COPTHTH008, COPTH.TH013 AS COPTHTH013,
                      COPTC.TC010 AS COPTCTC010, COPTC.TC011 AS COPTCTC011, COPTC.UDF02 AS COPTCUDF02, COPTC.UDF03 AS COPTCUDF03,
                      COPMA.MA002 AS COPMAMA002
    FROM       dbo.COPTG AS COPTG LEFT OUTER JOIN
                      dbo.COPTH AS COPTH ON COPTH.TH001 = COPTG.TG001 AND COPTH.TH002 = COPTG.TG002 LEFT OUTER JOIN
                      dbo.COPTC AS COPTC ON COPTC.TC001 = COPTH.TH014 AND COPTC.TC002 = COPTH.TH015 LEFT OUTER JOIN
                      dbo.COPMA AS COPMA ON COPMA.MA001 = COPTC.TC004
    WHERE     (COPTG.TG001 = '2301') AND (COPTG.TG003 > '20150101') AND (COPTG.TG004 LIKE 'a%') AND (COPTH.TH002 > '20150101001') AND (COPTG.TG023 = 'Y') AND
                      (COPTH.TH020 = 'Y') AND (COPTH.TH001 = '2301') AND (COPTC.TC027 = 'Y') AND (COPTC.TC003 > '20150101') AND (COPTC.TC001 = '2220') AND
                      (COPTC.TC004 LIKE 'a%')
	代理更新				  
	SELECT     SUBSTRING(COPTG.CREATE_DATE, 1, 8) AS COPTGCREATE_DATE, COPTG.TG003 AS COPTGTG003, COPTH.TH002 AS COPTHTH002, COPTH.TH004 AS COPTHTH004, 
                      COPTH.TH005 AS COPTHTH005, COPTH.TH006 AS COPTHTH006, COPTH.TH008 AS COPTHTH008, COPTH.TH013 AS COPTHTH013, COPTC.TC010 AS COPTCTC010, 
                      COPTC.TC011 AS COPTCTC011, COPTC.UDF02 AS COPTCUDF02, COPTC.UDF03 AS COPTCUDF03, COPMA.MA002 AS COPMAMA002
	FROM         dbo.COPTG AS COPTG LEFT OUTER JOIN
                      dbo.COPTH AS COPTH ON COPTH.TH001 = COPTG.TG001 AND COPTH.TH002 = COPTG.TG002 LEFT OUTER JOIN
                      dbo.COPTC AS COPTC ON COPTC.TC001 = COPTH.TH014 AND COPTC.TC002 = COPTH.TH015 LEFT OUTER JOIN
                      dbo.COPMA AS COPMA ON COPMA.MA001 = COPTC.TC004
	WHERE     (COPTG.TG001 = '2301') AND (COPTG.TG003 > '20150101') AND (COPTG.TG004 LIKE 'a%') AND (COPTH.TH002 > '20150101001') AND (COPTG.TG023 = 'Y') AND 
                      (COPTH.TH020 = 'Y') AND (COPTH.TH001 = '2301') AND (COPTC.TC027 = 'Y') AND (COPTC.TC003 > '20150101') AND (COPTC.TC001 = '2220') AND 
==============================
"""

import datetime

__author__ = 'Loffew'

"""
现在把代理[dl]和直营[zy]的销货数据分成两个视图
dl [年份 品号 单位 单价 总价 地址1 地址2 省份 代理商 代理商的客户（公司）]
zy [年份 品号 单位 单价 总价 地址1 地址2 省份 客户 部门 员工]
类作为视图的默认值设置，以检查视图方法是否把变量带入
其他：预置字段名的变量
"""


class ConnectPackage:
    def __init__(self):
        """
        self.start_year 默认为2015
        self.end_year 结束年，默认获取当年
        self.summary_object_name = ["水王子", "大众健康", "公共卫生", "国际业务", "销售服务", "工业"]
        
        self.title_name 网页head里面的title名字
        self.table_name 视图表的名字
        self.html_name 保存html后的前缀名
        """
        self.start_year = 2015
        self.end_year = datetime.date.today().year
        self.summary_object_name = ["水王子", "大众健康", "公共卫生", "国际业务", "销售服务", "工业"]

        self.title_name = "演示 标签"
        self.table_name = "演示 表名"
        self.html_name = "演示 文件名"
        

dbt_date = "COPTGTG003"
dbt_odd = "COPTHTH002"  # 新增  
dbt_article = "COPTHTH005"
dbt_number = "COPTHTH004"  # 新增
dbt_unit = "COPTHTH006"
dbt_per_unit = "COPTHTH008"
dbt_total_price = "COPTHTH013"
dbt_add1 = "COPTCTC010"
dbt_add2 = "COPTCTC011"
dbt_province = "COPTCUDF02"
dbt_agent = "COPTCUDF03"
dbt_client = "COPMAMA002"
dbt_depart = "CMSMEME002"
dbt_saler = "CMSMVMV002"


if __name__ == '__main__':
    print(", ".join((dbt_date, dbt_number)))
