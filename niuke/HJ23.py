# -*- coding: utf-8 -*-
# @Time : 2023/4/14 16:44
# @Author : ASUS
# @File : HJ23.py
# @Software: PyCharm

# 实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
#
# 数据范围：输入的字符串长度满足

str_in = input()

dict_key = set(str_in)

dic1 = {}
count = 0
for item in dict_key:
    for i in str_in:
        if item ==i:
            count+=1
    dic1[item] = count
    count = 0

min_num = 30
for item_dic in dic1.values():
    min_num = min(min_num,item_dic)

shachu = []
for item_dic2 in dic1.keys():
    if dic1[item_dic2] == min_num:
        shachu.append(item_dic2)

for letter in shachu:
    str_in = ''.join(str_in.split(letter))

print(str_in)