# -*- coding: utf-8 -*-
# @Time : 2023/4/14 9:28
# @Author : ASUS
# @File : HJ56.py
# @Software: PyCharm


# 完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
#
# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
#
# 例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

num = int(input())

def wanmeishu(num:int):
    yueshusum = 0
    for item in range(1,num):
        if num % item ==0:
            yueshusum +=item
    if yueshusum == num:
        return True
count = 0
for i in range(2,num+1):
    if wanmeishu(i):
        count+=1
print(count)