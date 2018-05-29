import xlsxwriter


def writeToExcel(info_dict):
    file_name = "本月考勤异常表"
    workbook = xlsxwriter.Workbook('./%s.xlsx' % file_name)
    worksheet = workbook.add_worksheet("考勤情况")
    worksheet.set_column('C:AG', 2.88)
    worksheet.freeze_panes(1, 1)
    ff = workbook.add_format({
        'bold': True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F4B084',  # 单元格背景颜色
    })
    nameb_ff = workbook.add_format({
        'border': 1,  # 单元格边框宽度
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#87CEFA',  # 单元格背景颜色
    })
    namea_ff = workbook.add_format({
        'border': 1,  # 单元格边框宽度
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#D1EEEE',  # 单元格背景颜色
    })
    label = workbook.add_format({
        'border': 1,  # 单元格边框宽度
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#CD6889',  # 单元格背景颜色
    })

    # 写好第一行
    ii = ["工号", "姓名", ]
    ii.extend([str(i) for i in range(1, 32)])

    for index, value in enumerate(ii):
        worksheet.write(0, index, value, ff)

    row = 1  # 第一行开始
    a = 2  # 合并单元格范围
    b = 3  # 合并单元格范围
    cc = 1

    for nn, ll in info_dict.items():
        if cc % 2:
            color = nameb_ff
        else:
            color = namea_ff
        cc += 1
        # 工号和姓名拆开
        rx, name = nn.split(",")
        # 合并单元格，2排2列
        aa = "A{}:A{}".format(a, b)
        bb = "B{}:B{}".format(a, b)
        worksheet.merge_range(aa, rx, color)
        worksheet.merge_range(bb, name, color)
        a += 2
        b += 2
        # 把数据写进去，ll 就是考勤列表
        for li in ll:  # li 是一个人的考勤列表
            if len(li[1]) != 0:
                worksheet.write(row, li[0] + 1, li[1], color)
            if len(li[2]) != 0:
                worksheet.write(row + 1, li[0] + 1, li[2], color)

        row += 2

    workbook.close()
