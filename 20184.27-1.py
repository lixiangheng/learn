'''python 脚本
检测局域网IP 并将能ping通的IP打印出来

'''

import os

list = []

ip1 = '10.10.19.'

# 生成IP，并组合，判断返回值
for ips in range(1, 254):
    ip = ip1 + str(ips)
    pingip = 'ping ' + ip
    if os.system(pingip) == 0:
        list.append(pingip)

print('ip %s 个数 %d ' % (list, len(list)))