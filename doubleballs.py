# -*- coding: cp936 -*-
import os
import sys
import random

# �������������
if len(sys.argv) == 2:
    p1 = sys.argv[1]
else:
    print('usage: redball.py seed_int ')
    sys.exit(1)

f1 = "100.txt"
if not os.path.exists(f1):
    print('ERROR: %s is not found.' % f1)
    sys.exit(1)


def mc(A, B):
    k = 0
    for a in A:
        if a in B:
            k += 1
    return k


#

A = [0 for i in range(0, 8)]  # ��ʼ��һ������6��0������,
# ���ѡ��6������
random.seed(p1)
reds = []
while len(reds) < 6:
    N = random.randint(1, 33)
    if N not in reds:
        reds.append(N)
print('random:', sorted(reds))

fp = open(f1, 'r')
alist = []
ln = 0
for line in fp:
    alist = line.strip().split(',')
    for i in range(1, 7):
        A[i] = int(alist[i])
    k = mc(reds, A[1:])
    if k > 3:
        ln += 1
        print(line.rstrip(), ':', k)
#
fp.close()
print('ln=', ln)