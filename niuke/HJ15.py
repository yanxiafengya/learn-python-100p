# -*- coding: utf-8 -*-
# @Time : 2023/4/11 20:51
# @Author : ASUS
# @File : HJ15.py
# @Software: PyCharm
# 输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
#
# # 数据范围：保证在 32 位整型数字范围内
num = int(input())
binnun =bin(num)+''
# print(binnun)
# print(type(binnun))
count = 0
for i in binnun[2:]:

    if int(i) ==1:
        count+=1
print(count)