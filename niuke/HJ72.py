# -*- coding: utf-8 -*-
# @Time : 2023/4/13 21:48
# @Author : ASUS
# @File : HJ72.py
# @Software: PyCharm


input()
for i in range(0,21):
    for j in range(0,34):
            if 5*i + 3*j +(100-i-j)*1/3 ==100 and i+j <=100 :
                print(i,j,100-i-j)
