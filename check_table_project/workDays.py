import os
import datetime
import xlrd


def workTime():
    """
    维护一张日程表,从表获取工作日
    ["date", "date",]
    """
    TODAY = datetime.date.today()

    point = input("考勤表月份[数字]，默认为当月：")
    try:
        point = int(point)
        MONTH = str(TODAY)[:5] + "%02d" % point + "-"
    except ValueError:
        print("默认为当月")
        point = TODAY.month
        MONTH = str(TODAY)[:8]

    FILEPATH = "./workday.xlsx"
    if os.path.exists(FILEPATH):
        table = xlrd.open_workbook(FILEPATH)
        sheet = table.sheets()[0]

        work_table = sheet.row_values(point)[1:]
        work_table = ["%02d" % int(i) for i in work_table if i]
        work_table = [MONTH + i for i in work_table]
        return work_table
    else:
        print("检查文件 %s 是否存在" % FILEPATH)
