# -*- coding: utf-8 -*-
# @Time : 2023/4/13 18:05
# @Author : ASUS
# @File : HJ81.py
# @Software: PyCharm

str_short =input()
str_long =input()

flag = 0
for item in str_short:
    if item not in str_long:
        print('false')
        flag =1
        break
if flag == 0:

    print('true')



