# -*- coding: utf-8 -*-
# @Time : 2023/4/13 11:58
# @Author : ASUS
# @File : HJ85.py
# @Software: PyCharm
str_in = list(input())
max = 0
for i in range(len(str_in)):
    for j in range(i,len(str_in)):
        if str_in[i:j+1] == str_in[i:j+1][::-1] and j-i+1>max:
            max = j-i+1

print(max)

# for i in str_in:
#     for j in daoxu:
#         if i == j:
