import xlrd


def getCheckIn():
    """
    对打卡机导出的表进行汇总统计
    [['number', 'name', 'date', '上午时间', '下午时间'],]
    :return:
    """
    table = xlrd.open_workbook("./attendance.xls")
    sheet_4 = table.sheet_by_name(u'异常统计')
    rows_4 = sheet_4.nrows

    info_list = []

    for i in range(4, rows_4):
        ll = sheet_4.row_values(i)[:6]
        ll[0] = ll[0].upper()
        del ll[2]
        info_list.append(ll)

    return info_list


def workStatusB(ll):
    if len(ll[3]):
        if ll[3] <= '09:00':
            ll[3] = ""
        else:
            ll[3] = "迟"
    else:
        ll[3] = "未"

    if len(ll[4]):
        if ll[4] >= '17:30':
            ll[4] = ""
        else:
            ll[4] = "退"
    else:
        ll[4] = "未"

    return ll


def workStatusA(ll):
    if len(ll[3]):
        if ll[3] <= '08:30':
            ll[3] = ""
        else:
            ll[3] = "迟"
    else:
        ll[3] = "未"

    if len(ll[4]):
        if ll[4] >= '17:00':
            ll[4] = ""
        else:
            ll[4] = "退"
    else:
        ll[4] = "未"

    return ll


if __name__ == '__main__':
    pass

