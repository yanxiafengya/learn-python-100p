# -*- coding: utf-8 -*-
# @Time : 2023/4/11 15:28
# @Author : ASUS
# @File : hj6.py
# @Software: PyCharm

# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

# list1 =[]
# if num == 1:
#     print()
#
# else:
#     while num >1:
#         for i in range(2,int(math.sqrt(num)+1)):
#             if num % i ==0:
#                 list1.append(str(i))
#                 num = int(num/i)
#                 break
# print((' ').join(list1))
import math
num = int(input())
def zhishu(innernum):
    flag = 0
    for item in range(2,int(innernum**(0.5)+1)):
        if innernum % item == 0:
            print(item,end=' ')
            flag = 1
            temp = int(innernum/item)
            if temp >1:
                zhishu(temp)
                break
    if flag == 0:
        print(innernum)

zhishu(num)