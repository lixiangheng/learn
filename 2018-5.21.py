# 删除moloch不是这两天的数据抓包文件
import os
import re
import time


times = time.strftime('%Y%m%d')
newtimes = times[2:]
uptimes = int(newtimes)-1

for i in os.listdir('/opt/test/'):
    c = re.search(newtimes, i)
    d = re.search(uptimes, i)
    if c is None and d is None:
        dels = 'rm -rf ' + i
        os.chdir('/opt/test/')
        if os.system(dels) == 0:
            print('清理空间成功')
        else:
            print('不需要清理')