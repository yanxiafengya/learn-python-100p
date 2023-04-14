# -*- coding: utf-8 -*-
# @Time : 2023/4/14 12:50
# @Author : ASUS
# @File : HJ35.py
# @Software: PyCharm

# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
# 例如，当输入5时，应该输出的三角形为：
# 1 3 6 10 15
# 2 5 9 14
# 4 8 13
# 7 12
# 11

int_in = int(input())
count =1
lis =[[0 for i in range(int_in)] for j in range(int_in)]
lis_out = []
# print(lis)
for i in range(int_in):
    row = i
    col =0
    while(row >=0 and col<=int_in-1):
        lis[row][col] = count
        count+=1
        row-=1
        col+=1
for index1,item1 in enumerate(lis):
    for index2,item2 in enumerate(item1):
        if index1+index2<=int_in-1:
            print(item1[index2],end=' ')
    print()