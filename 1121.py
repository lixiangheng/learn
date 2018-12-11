# 自己读取excel试卷阅卷
import xlrd
import xlwt
import os
import time
import win32com.client

start_time = time.clock()
daan = ['B', 'A', 'A', 'C', 'C', 'A', 'C', 'C', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'A', 'D', 'B', 'D', 'D', 'A', 'B',
        'D', 'C', 'D', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'B', 'B', 'D', 'B', 'A', 'A', 'C', 'D', 'B', 'B', 'B', 'A',
        'A', 'C', 'D', 'D', 'A', 'C', 'D', 'A', 'C', 'D', 'C', 'C', 'D', 'A', 'D', 'A', 'A', 'B', 'B', 'A', 'B', 'B',
        'A', 'B', 'B', 'A', 'B', 'B', 'A', 'D', 'B', 'B', 'D', 'D', 'A', 'B', 'D', 'B', 'C', 'D', 'C', 'A', 'A', 'D',
        'C', 'A', 'D', 'B', 'C', 'A', 'B', 'A', 'A', 'A', 'C', 'C', 'D', 'D', 'A', 'B', 'D', 'C', 'A', 'D', 'D', 'D',
        'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'A', 'C', 'C', 'D', 'C', 'A', 'D', 'C', 'D', 'A', 'D', 'C', 'B', 'D',
        'A', 'B', 'A', 'D', 'C', 'B', 'A', 'A', 'D', 'A', 'B', 'B', 'A', 'C', 'A', 'C', 'D', 'A', 'D', 'A', 'D', 'B',
        'A', 'D', 'B', 'A', 'C', 'C', 'D', 'B', 'B', 'A', 'D', 'C', 'D', 'B', 'A', 'C', 'B', 'D', 'B', 'A', 'B', 'B',
        'A', 'A', 'D', 'A', 'C', 'A', 'D', 'D', 'C', 'D', 'A', 'D', 'D', 'A', 'A', 'B', 'B', 'D', 'C', 'C', 'C', 'C',
        'A', 'B', 'D', 'D', 'C', 'D', 'D', 'B', 'A', 'B', 'D', 'D', 'D', 'C', 'A', 'C', 'B']


# filename = []
# for wenjian in os.listdir("D:\\Python\\Auto\\11\\timu"):
#     filename.append(wenjian)

filelist = [wenjian for wenjian in os.listdir("D:\\Python\\Auto\\11\\timu2")]


fenshu = {}

for file in filelist:
    score = 0
    timu = []

    # 读取试卷答案
    os.chdir("D:\\Python\\Auto\\11\\timu2")
    # number = [x for x in range(2, 217)]
    # 没有密码用这个
    try:
        # xlApp = win32com.client.Dispatch("Excel.Application")
        # filename, password = "D:\\Python\\Auto\\11\\timu2\\" + file, ''
        # xlwb = xlApp.Workbooks.Open(filename, False, True, None, Password=password)
        # # print(xlwb.Sheets(1).Cells(3, 8).value)
        # for i in range(3, 218):
        #     timu.append(xlwb.Sheets(1).Cells(i, 8).value)
        openexcel = xlrd.open_workbook(file).sheet_by_index(0)
        for i in range(2, 217):
            timu.append(openexcel.cell(i, 7).value)
    # 有密码用这个

    except xlrd.biffh.XLRDError:
        xlApp = win32com.client.Dispatch("Excel.Application")
        filename, password = "D:\\Python\\Auto\\11\\timu2\\" + file, '8008105119'
        xlwb = xlApp.Workbooks.Open(filename, False, True, None, Password=password)
        # print(xlwb.Sheets(1).Cells(3, 8).value)
        for i in range(3, 218):
            timu.append(xlwb.Sheets(1).Cells(i, 8).value)
    #

    # timua = [x.upper() for x in timu]
        # 判断答案是否正确
    for a, b in zip(daan, timu):
        if b is None or type(b) is float:
            if a == b:
                score += 1
        else:
            if a == b.upper():
                score += 1
        # except AttributeError:
        #     print(AttributeError)
    fenshu[file] = score

zo = 0
ko = 0

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')

for x, y in fenshu.items():
    sheet.write(zo, 0, x)
    sheet.write(ko, 1, y)
    zo += 1
    ko += 1

    print("%s : %s " % (x, y))

book.save('xx.xlsx')
end_time = time.clock()

print("时间 :%s" % (end_time-start_time))