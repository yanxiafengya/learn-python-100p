# -*- coding: utf-8 -*-
# @Time : 2023/4/9 19:54
# @Author : ASUS
# @File : hj3.py
# @Software: PyCharm

# 明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

lines = int(input())
a_set = set()
for i in range(lines):
    a_set.add(int(input()))
# print(a_set)

# list = list(a_set).sort()
list = list(a_set)
list.sort()
# print('list ',list)
for li in list:
    print(li)

