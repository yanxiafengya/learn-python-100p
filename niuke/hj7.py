# -*- coding: utf-8 -*-
# @Time : 2023/4/11 16:57
# @Author : ASUS
# @File : hj7.py
# @Software: PyCharm

# HJ7 取近似值
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
#
# 数据范围：保证输入的数字在 32 位浮点数范围内
num = float(input())
str_1 = str(num)

int_1 = int(str_1.split('.')[0])
xiaoshu = str_1.split('.')[1]
str_2 = '0.' +xiaoshu
if (float(str_2) -0.5) >=0:
    int_1 +=1

print(int_1)
# print(int_1)