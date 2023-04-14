# -*- coding: utf-8 -*-
# @Time : 2023/4/12 20:54
# @Author : ASUS
# @File : pj102.py
# @Software: PyCharm

# 输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
str_in = input()
dict_1 = {}
for item in str_in:
    if item not in dict_1.keys():
        dict_1[item] = 1
    else:
        dict_1[item] +=1

dict_1 = dict(sorted(dict_1.items() ,key= lambda x:(-x[1],x[0])))

for key in dict_1.keys():
    print(key,end='')