# -*- coding: utf-8 -*-
# @Time : 2023/4/13 11:47
# @Author : ASUS
# @File : HJ86.py
# @Software: PyCharm
# 求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

num = int(input())
binnum = bin(num)
print(binnum)
str_list = binnum[2:].split('1')
print(str_list)
max = 0
for item in str_list:
    if len(item) >max:
        max = len(item)
print(max)