# -*- coding: utf-8 -*-
# @Time : 2023/4/13 12:36
# @Author : ASUS
# @File : HJ84.py
# @Software: PyCharm

str_in = input()
count = 0
for item in str_in:
    if ord('A')<=ord(item)<=ord("Z"):
        count+=1
print(count)
