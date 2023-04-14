# -*- coding: utf-8 -*-
# @Time : 2023/4/13 8:24
# @Author : ASUS
# @File : HJ96.py
# @Software: PyCharm

# 将一个字符串中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。

# Jkdi234klowe90a3
import re
str_in = input()
# new_str = ''
# for i in range(1,len(str_in)+1):
#     try:
#         if (i ==1 and str_in[i-1].isdigit()):
#             new_str += '*'
#         new_str +=str_in[i-1]
#         if (i == len(str_in) and str_in[i-1].isdigit()):
#             new_str +='*'
#         if (str_in[i-1].isdigit() and (str_in[i].isdigit() ==False)):
#             new_str +='*'
#         if (str_in[i-1].isdigit() == False) and str_in[i].isdigit():
#             new_str +='*'
#     except:
#         pass
# print(new_str)

# re.sub('(\d+)', addstar, input()