# -*- coding: utf-8 -*-
# @Time : 2023/4/11 17:55
# @Author : ASUS
# @File : hj9.py
# @Software: PyCharm

# 输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# 保证输入的整数最后一位不是 0 。

num = input()
daozhuan = num[::-1]
temp = []
for i in daozhuan:
    if i not in temp:
        temp.append(i)
output = ''.join(temp)
print(output)