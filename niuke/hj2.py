# -*- coding: utf-8 -*-
# @Time : 2023/4/9 19:46
# @Author : ASUS
# @File : hj2.py
# @Software: PyCharm

# 描述
# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

str = input('').lower()
zifu = input('').lower()
num = 0
for s in str:
    if s == zifu:
        num+=1
print(num)