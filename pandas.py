import pandas as pd
import datetime

read_table = pd.read_excel('test.xlsx', '2020目录', header=1)

col_datetime = read_table['评审完成时间']
col_total = read_table['总金额']
col_gross = read_table['1~6月合同毛利']

# 年月日期格式转换
month = []
for i in col_datetime:
    z = str(i).split()
    s = z[0]
    new_format = datetime.datetime.strptime(s, "%Y-%m-%d").strftime("%Y-%m")
    if new_format == "2020-01":
        new_format = "一月"
    elif new_format == "2020-02":
        new_format = "二月"
    elif new_format == "2020-03":
        new_format = "三月"
    elif new_format == "2020-04":
        new_format = "四月"
    elif new_format == "2020-05":
        new_format = "五月"
    elif new_format == "2020-06":
        new_format = "六月"
    month.append(new_format)

# 合成生成新的DataFrame
new_table = {"月份": month, "总金额": col_total, "毛利": col_gross}
frame = pd.DataFrame(new_table)

person = read_table.groupby('签订人')[['总金额', '1~6月合同毛利']].sum()
business = read_table.groupby('一级行业_商机')[['总金额', '1~6月合同毛利']].sum()
pact = read_table.groupby(['合同类型', '客户名称'])[['总金额', '1~6月合同毛利']].sum()
data1 = frame.groupby('月份')[['总金额', '毛利']].sum()
ls = ['一月', '二月', '三月', '四月', '五月', '六月']
data1 = data1.reindex(index=ls)

write = pd.ExcelWriter('month.xlsx', engine="openpyxl")
read_table.to_excel(write, '产品销售')
person.to_excel(write, '按人员统计')
pact.to_excel(write, '按合同统计')
data1.to_excel(write, '按月统计')
business.to_excel(write, '按行业')

write.save()
