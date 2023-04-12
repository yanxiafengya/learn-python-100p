# -*- coding: utf-8 -*-
# @Time : 2023/4/11 20:38
# @Author : ASUS
# @File : HJ14.py
# @Software: PyCharm

# 给定 n 个字符串，请对 n 个字符串按照字典序排列。

num = int(input())
list_1 = []
for i in range(num):
    list_1.append(input())

list_3 = sorted(list_1)
# print(list_3)
for item in list_3:
    print(item)