# -*- coding: utf-8 -*-
# @Time : 2023/4/12 19:40
# @Author : ASUS
# @File : hj108.py
# @Software: PyCharm
# 正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

lis = input()
num1 = int(lis.split(' ')[0])
num2 = int(lis.split(' ')[1])
minnum= min(num1,num2)
gongyueshu = []

while True:
    flag = 0
    for i in range(2,int(minnum) +1):
        if num1 % i ==0 and num2 %i ==0:
            gongyueshu.append(i)
            num1=num1/i
            num2=num2/i
            minnum = minnum/i
            flag =1
            break
    if flag ==0:
        break
outnum=1
for number in gongyueshu:
    outnum *= int(number)
outnum = int(outnum * num1 * num2)
print(outnum)

