# -*- coding: utf-8 -*-
# @Time : 2023/4/14 16:59
# @Author : ASUS
# @File : HJ22.py
# @Software: PyCharm

# 某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
# 小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。

# while True:
#     n = int(input())
#     if n ==0:
#         break
#     else:
#         dri_num = int((n-(n%2))/2)
#         print(dri_num)

def dri(n:int):
    if n ==0 or n ==1:
        return 0
    if n>=2:
        return dri(n-2)+1

while True:
    n = int(input())
    if not n:
        break

    else:
        print(dri(n))