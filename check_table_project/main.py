from getCheckIn import getCheckIn, workStatusB, workStatusA
from getStaff import getStaffKinds
from workDays import workTime
from writeExcel import writeToExcel


def work_condition(pack_list):
    """
    过滤掉非异常信息，并把异常信息变成对应的值，返回结果
    :param pack_list:
    :return:
    """
    if staff_dict.get(pack_list[0]) == "A":
        return workStatusA(pack_list)

    elif staff_dict.get(pack_list[0]) == "B":
        return workStatusB(pack_list)

    else:
        return False


def getStaffDict(info_list):
    """
    按上下班种类清洗
    :param info_list:
    :return: {"number, name":[[info],[info]]}
    """
    staff_status_dict = {}
    for i in info_list:
        i = work_condition(i)
        if i:
            rx, name, date, before, after = i
            date = int(date[-2:])
            head = ",".join([rx, name])
            body = [date, before, after]
            
            if head in staff_status_dict:
                staff_status_dict.get(head).append(body)
            else: staff_status_dict[head] = [[date, before, after]]
    return staff_status_dict


if __name__ == '__main__':

    staff_dict = getStaffKinds()  # {Number: class}

    check = getCheckIn()  # [['number', 'name', 'date', '上午时间', '下午时间'],]

    work = workTime()  # ["date", "date",]

    check_list = [i for i in check if i[0] in staff_dict.keys() and i[2] in work]  # 把不在职员工或非工作日的记录清洗掉

    dic = getStaffDict(check_list)  # 清洗一次

    writeToExcel(dic)

