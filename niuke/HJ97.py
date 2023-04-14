# -*- coding: utf-8 -*-
# @Time : 2023/4/12 21:44
# @Author : ASUS
# @File : HJ97.py
# @Software: PyCharm

# 首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。
# 0即不是正整数，也不是负数，不计入计算。如果没有正数，则平均值为0。

count = int(input())
fushu = 0
zhengshu = []
lis = input().split(' ')
for item in lis:
    if int(item)<0:
        fushu+=1
    elif int(item)>0:
        zhengshu.append(int(item))
if len(zhengshu)==0:
    avgnum =0.0
else:
    avgnum = round(sum(zhengshu)/len(zhengshu),1)
print(fushu,avgnum)


