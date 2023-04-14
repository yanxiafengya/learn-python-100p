# -*- coding: utf-8 -*-
# @Time : 2023/4/14 10:03
# @Author : ASUS
# @File : hj53.py
# @Software: PyCharm

# 以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数、左上角数和右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。


lis = [2,3,2,4]

# 0<=i行下标<=2*i-2

line = int(input())

if line <=2:
    print('-1')
else:
    print(lis[(line-3) %4])

