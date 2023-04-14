# -*- coding: utf-8 -*-
# @Time : 2023/4/13 22:14
# @Author : ASUS
# @File : hj62.py
# @Software: PyCharm
# 输入一个正整数，计算它在二进制下的1的个数。
while True:
    try:
        num = int(input())
        binnum = bin(num)[2:]
        lis = binnum.split('0')


        print(len(''.join(lis)))
    except:
        break