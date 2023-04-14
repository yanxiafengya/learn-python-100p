# -*- coding: utf-8 -*-
# @Time : 2023/4/12 21:38
# @Author : ASUS
# @File : hj99.py
# @Software: PyCharm

# 自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数

n_input = int(input())
length = 0
count = 0
for i in range(n_input+1):
    length = len(str(i))
    if str(i*i)[-length:] == str(i):
        count+=1
print(count)