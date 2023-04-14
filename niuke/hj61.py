# -*- coding: utf-8 -*-
# @Time : 2023/4/13 23:23
# @Author : ASUS
# @File : hj61.py
# @Software: PyCharm
def fun1(m,n):
    if m<0 or n <0:
        return 0
    elif m==1 or n ==1:
        return 1
    else:
        return fun1(m,n-1)+fun1(m-n,n)

m,n = map(int,input().split(' '))
print(m,n)
print(fun1(m,n))

