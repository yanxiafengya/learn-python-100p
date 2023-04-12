# -*- coding: utf-8 -*-
# @Time : 2023/4/11 21:04
# @Author : ASUS
# @File : HJ16.py
# @Software: PyCharm
# 输入的第 1 行，为两个正整数N，m，用一个空格隔开：
# 每行有 3 个非负整数 v p q
#
#
# （其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
# 输入：
# 50 5
# 20 3 5
# 20 3 5
# 10 3 0
# 10 2 0
# 10 1 0


# 1000 5
# 300 5 0
# 400 2 0
# 300 5 2
# 300 4 2
# 600 4 0



# 复制
# 输出：
# 130
import math
list_str= input().split(' ')
# print(list_str)
n,m = list_str
# n背包容量
n = int(int(n)/10)
# m可购买的物体数量
m = int(m)
# 声明一个数组存放物品的重量
weight =[[0 for col in range(3)] for row in range(m+1)]
# 声明一个数组存放物品的满意度
value =[[0 for col in range(3)] for row in range(m+1)]




for line in range(1,m+1):
    str_input = input()
    # 物品的重量
    v= int(int(str_input.split(' ')[0])/10)
    # 物品的满意度
    p= v* int(str_input.split(' ')[1])
    # 物品的主附件
    q= int(str_input.split(' ')[2])
    if q==0:
        weight[line][0]=v
        value[line][0]= p
    elif weight[q   ][1] ==0:
        weight[q][1] = v
        value[q][1] = p
    else:
        weight[q][2] = v
        value[q][2]=p

    # print(v,p,q)
    # print(weight,value)

result = [[0 for col in range(n+1)] for row in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if j<weight[i][0]:
            result[i][j] = result[i-1][j]

        elif j >=weight[i][0] and \
                j < weight[i][0] + weight[i][1] and\
                j < weight[i][0] + weight[i][2]:

            result[i][j] = max(result[i-1][j],
                               result[i-1][j-weight[i][0]]+value[i][0]
                               )

        elif j >=weight[i][0] and \
                j >= weight[i][0] + weight[i][1] and \
                j < weight[i][0] + weight[i][2]:

            result[i][j] = max(result[i-1][j],
                               result[i-1][j-weight[i][0]]+value[i][0],
                               result[i-1][j-weight[i][0]-weight[i][1]]+value[i][0]+value[i][1]
                               )

        elif j >=weight[i][0] and \
                j >= weight[i][0] + weight[i][2] and \
                j < weight[i][0] + weight[i][1]:

            result[i][j] = max(result[i-1][j],
                               result[i-1][j-weight[i][0]]+value[i][0],
                               result[i-1][j-weight[i][0]-weight[i][2]]+value[i][0]+value[i][2])

        elif j >=weight[i][0] and \
                j >= weight[i][0] + weight[i][2] and \
                j >= weight[i][0] + weight[i][1] and \
                j < weight[i][0]+weight[i][1]+weight[i][2]:

            result[i][j] = max(result[i-1][j],
                               result[i-1][j-weight[i][0]]+value[i][0],
                               result[i-1][j-weight[i][0]-weight[i][1]]+value[i][0]+value[i][1],
                               result[i-1][j-weight[i][0]-weight[i][2]]+value[i][0]+value[i][2])

        else:

            result[i][j] = max(result[i-1][j],
                               result[i-1][j-weight[i][0]]+value[i][0],
                               result[i-1][j-weight[i][0]-weight[i][1]]+value[i][0]+value[i][1],
                               result[i-1][j-weight[i][0]-weight[i][2]]+value[i][0]+value[i][2],
                               result[i-1][j-weight[i][0]-weight[i][1]-weight[i][2]]+value[i][0]+value[i][1]+value[i][2])


print(result[m][n]*10)
# print('最后___',weight,value)

