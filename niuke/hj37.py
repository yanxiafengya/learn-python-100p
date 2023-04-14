# -*- coding: utf-8 -*-
# @Time : 2023/4/14 12:21
# @Author : ASUS
# @File : hj37.py
# @Software: PyCharm

n = int(input())

lis = [1,1]
if n>2:
    for i in range(n-2):
        lis.append(lis[i]+lis[i+1])
print(lis[-1])