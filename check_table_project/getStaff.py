import os
import xlrd


def getStaffKinds():
    """
    在员工信息获取工号对应的上下班种类，对应成字典并返回
    [编号, 上下班种类]
    """
    filepath = "./员工信息.xlsx"
    if os.path.exists(filepath):
        staff_dict = {}
        table = xlrd.open_workbook(filepath)
        sheet_1 = table.sheet_by_name(u'在职人员')
        rows_1 = sheet_1.nrows
        for row in range(1, rows_1):
            table_row = sheet_1.row_values(row)
            staff_dict[table_row[1]] = table_row[3]
        return staff_dict

    text = "检查 员工信息表 是否在当前文件夹"
    print(text)



