# -*- coding: utf-8 -*-
# @Time : 2023/4/12 21:19
# @Author : ASUS
# @File : HJ100.py
# @Software: PyCharm

# 等差数列 2，5，8，11，14。。。。
# （从 2 开始的 3 为公差的等差数列）
# 输出求等差数列前n项和
shuliesum = 0
n = int(input())
for i in range(n):
    shuliesum +=  i*3+2
print(shuliesum)
