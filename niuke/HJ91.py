# -*- coding: utf-8 -*-
# @Time : 2023/4/13 9:20
# @Author : ASUS
# @File : HJ91.py
# @Software: PyCharm

def fun(m,n):
    if m<0 or n <0:
        return 0
    elif m==0 and n==0:
        return 1
    else:
        return fun(m-1,n)+fun(m,n-1)

m,n = map(int,input().split(' '))
print(fun(m,n))
