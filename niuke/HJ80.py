# -*- coding: utf-8 -*-
# @Time : 2023/4/13 18:16
# @Author : ASUS
# @File : HJ80.py
# @Software: PyCharm

# 将两个整型数组按照升序合并，并且过滤掉重复数组元素。
# 输出时相邻两数之间没有空格。
input()
lis1=input().split(' ')
input()
lis2=input().split(' ')

lis3 = list(set(lis1 + lis2))

lis4 =[]

for li in lis3:
    lis4.append(int(li))
# print(lis4)
lis5=sorted(lis4)

# print(lis5)
str_out =''
for inst in lis5:
    str_out += str(inst)
print(str_out)






