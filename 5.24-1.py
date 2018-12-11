# 猜大小游戏

import random


def dice(c=0, zhi=None):
    if zhi is None:
        total = []
        while c < 3:
            total.append(random.randint(1, 7))
            c += 1
        return total


def panduan(zhi):
    if 11 <= zhi <= 18:
        return '大'
    if 3 <= zhi <=10:
        return '小'


def panduantext(zhi):
    if zhi == '大':
        return '大'
    elif zhi == '小':
        return '小'


def start():
    fen = 100
    while fen > 0:
        print('-----------猜数字-----------')
        aa = int(input('请押分：'))
        bb = int(input('请选择要押大小还是数字：1、大小 2、数字： '))
        cc = sum(dice())
        if bb == 1:
            dd = input('请押大小： ')
            print('你押的是大小开出结果%s ' % panduan(cc))
            if panduantext(dd) == panduan(cc):
                fen += (aa * 2)
                print('你中奖了，现在的分数:%s' % fen)
            else:
                fen -= aa
                print('你没有中奖!现在的分数:%s' % fen)
        elif bb == 2:
            ee = int(input('请押数字： '))
            print('你押的是数字开出结果%s ' % panduan(cc))
            if ee == cc:
                fen += (aa * 10)
                print('你中奖了，现在的分数:%s' % fen)
            elif panduan(ee) == panduan(cc):
                fen += (aa * 2)
                print('你中奖了，现在的分数:%s' % fen)
            else:
                fen -= aa
                print('你没有中奖!现在的分数:%s' % fen)



start()


