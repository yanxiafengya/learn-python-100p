# -*- coding: utf-8 -*-
# @Time : 2023/4/14 12:07
# @Author : ASUS
# @File : HJ40.py
# @Software: PyCharm


str_in = input()
# print(str_in)
num_letter = 0
num_space = 0
num_num = 0
other_num = 0
for i in str_in:
    # 判断中英文字符
    if i.isalpha():
        num_letter+=1
    elif i ==' ':
        num_space+=1
    # 判断数字
    elif i.isdigit():
        num_num+=1
other_num = len(str_in)-num_letter-num_space-num_num
print(num_letter)
print(num_space)
print(num_num)
print(other_num)