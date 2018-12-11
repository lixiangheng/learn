'''
文件备份脚本
'''

import time
import os


def shijian():
    z = str('.tar.gz')
    a = time.strftime('%Y%m%d')
    c = a + z
    return c


os.chdir('/root/')
filename = os.listdir('.')
for i in filename:
    if shijian() == i:
        print('文件已备份%s' % i)
        break
else:
    os.chdir('/opt/log/')
    order = 'tar -cvf /root/' + shijian() + ' access_log'
    if os.system(order) == 0:
        print('备份成功')


