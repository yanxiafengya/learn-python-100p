# -*- coding: utf-8 -*-
# @Time : 2023/4/13 23:42
# @Author : ASUS
# @File : HJ60.py
# @Software: PyCharm

# 任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

def prime(num:int):
    count = 0
    for item in range(1,num+1):
        if num % item ==0:
            count+=1
    if count == 2:
        return True


num = int(input())
chazhi = 1000
list1=[0,0]
for i in range(2,num):
    if prime(i) and prime(num-i) and abs(num-i-i)<chazhi:
        chazhi = abs(num-i-i)

        list1[0]=i
        list1[1]=num-i


list1 = sorted(list1)
print(list1[0])
print(list1[1])