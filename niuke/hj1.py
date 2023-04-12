# -*- coding: utf-8 -*-
# @Time : 2023/4/9 19:38
# @Author : ASUS
# @File : hj1.py
# @Software: PyCharm
# 描述
# 计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
# 输入描述：

# 第一种解法
# import sys
#
# line = sys.stdin.readline()
# a = line.split(' ')
# print(len(a[-1])-1)

# 第二种解法：
str = input()
length = len(str.split(' ')[-1])
print(length)