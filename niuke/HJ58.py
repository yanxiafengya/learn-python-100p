# -*- coding: utf-8 -*-
# @Time : 2023/4/14 18:13
# @Author : ASUS
# @File : HJ58.py
# @Software: PyCharm

# 输入n个整数，找出其中最小的k个整数并按升序输出
# 本题有多组输入样例

while True:
    try:
        lis =[]
        n,k = map(int,input().split(' '))
        num_lis = input().split(' ')
        for i in num_lis:
            lis.append(int(i))

        lis.sort()

        for i in range(k):
            print(lis[i],end=' ')


    except:
        break