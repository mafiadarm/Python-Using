import datetime


def getWeek(ll):
    """日期所在时间是周几，如果是周一到周五，则返回True"""
    day = ll[3].split("-")
    day = "".join(day)
    week = datetime.datetime.strptime(day, "%Y%m%d").weekday()
    if 0 <= week <= 4:
        return True
