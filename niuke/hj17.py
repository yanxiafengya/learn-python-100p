# -*- coding: utf-8 -*-
# @Time : 2023/4/12 18:33
# @Author : ASUS
# @File : hj17.py
# @Software: PyCharm
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
# 从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
import re
str_in = input()
list_in = str_in.split(';')[:-1]
# print(list_in)
rec = re.compile('[A,D,W,S][0-9]{1,2}$')
list_out = []
for item in list_in:
    if rec.match(item):
        list_out.append(item)
# print(list_out)
list_zuobiao = [0,0]
for item1 in list_out:
    # print(item1[1:])
    if item1[0] =='A':
        list_zuobiao[0] -= int(item1[1:])
    elif item1[0] =='D':
        list_zuobiao[0] += int(item1[1:])
    elif item1[0] =='W':
        list_zuobiao[1] += int(item1[1:])
    else:
        list_zuobiao[1] -= int(item1[1:])
print(str(list_zuobiao[0])+','+str(list_zuobiao[1]))



