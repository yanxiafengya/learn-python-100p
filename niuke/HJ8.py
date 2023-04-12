# -*- coding: utf-8 -*-
# @Time : 2023/4/11 17:10
# @Author : ASUS
# @File : HJ8 合并表记录.py
# @Software: PyCharm
# 数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
num = int(input())
dict_1 = {}
for i in range(0,num):
    list_temp = input()
    key = list_temp.split(' ')[0]
    value = int(list_temp.split(' ')[1])

    if key not in dict_1.keys():
        dict_1[key] = value

    else:
        dict_1[key] = dict_1[key] +value
dict_2 = dict(sorted(dict_1.items(),key= lambda x:int(x[0])))
# print(dict_2)
for item,value in dict_2.items():
    print(int(item),value)
