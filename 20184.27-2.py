'''运维派提供外出企业项目实践机会（第6次）来了（本月中旬），但是，名额有限，队员限3人（班长带队）。

因此需要挑选学生，因此需要一个抓阄的程序：

要求：

1、执行脚本后，想去的同学输入英文名字全拼，产生随机数01-99之间的数字，数字越大就去参加项目实践，前面已经抓到的数字，下次不能在出现相同数字。
2、第一个输入名字后，屏幕输出信息，并将名字和数字记录到文件里，程序不能退出继续等待别的学生输入。'''


import random

# 获取随机数字1-99不重复


dit = {}

while True:
    name = input("输入你的名字的拼音：")
    if name == 'quit':
        break
    if name.isspace() or len(name) == 0:
        print("不能为空，请重新输入！")
    else:
        dit[name] = (random.sample(range(1, 99+1), 1))
  
# 词典排序，生成新的词典
dit2 = sorted(dit.items(), key=lambda x: x[1], reverse=True)


print(dit2)

for to in dit2[:3]:
    print("姓名: %s, 随机号%s" % (to[0], to[1]))
