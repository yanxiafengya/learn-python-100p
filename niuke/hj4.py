# -*- coding: utf-8 -*-
# @Time : 2023/4/9 20:21
# @Author : ASUS
# @File : hj4.py
# @Software: PyCharm

# HJ4 字符串分隔
# 描述
# •输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
#
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

str = input()
# list_1 = list(str)
# for i,itm in ()
while len(str)>8:
    print(str[:8])
    str = str[8:]
list_1 = str.ljust(8,'0')
print(list_1)