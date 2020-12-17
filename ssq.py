
import random
import sys

i= 0
try:
    y = int(input('请输入要选择的注数：'))
    # y = int(sys.argv[1])
except ValueError:
    print('请输入数字！')

while i < y:
    red = random.sample(range(1, 34), 6)
    blue = random.sample(range(1, 17), 1)
    red.sort()
    print("%s - %s" %(str(red), str(blue)))
    i +=1
