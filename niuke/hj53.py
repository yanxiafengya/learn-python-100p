# -*- coding: utf-8 -*-
# @Time : 2023/4/14 10:03
# @Author : ASUS
# @File : hj53.py
# @Software: PyCharm

# 以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数、左上角数和右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。

sanjiao = [[0],[1]]
lis = []

# 0<=i行下标<=2*i-2

line = int(input())

for i in range(2,line+1):
    lis = [0 for item in range(2 * i - 2 + 1)]
    for j in range(0,2*i-2+1):


        if j==0:


            # lis.append(0 + 0 + sanjiao[i-1][j])
            lis[j] = 0+0+sanjiao[i-1][j]



        elif j ==1 and j == 2*(i-1)-1:
            lis[j] = 0 + sanjiao[i - 1][j - 1] +0
        elif j ==1:
            # lis.append(0 +sanjiao[i-1][j-1]+sanjiao[i-1][j])

            lis[j] = 0 + sanjiao[i-1][j-1] + sanjiao[i - 1][j]
        elif j == 2*(i-1)-1:
            lis[j] = sanjiao[i-1][j-2]+ sanjiao[i - 1][j - 1] + 0

        elif j == 2*(i-1):
            lis[j] = sanjiao[i - 1][j - 2] + 0 + 0
        else:
            lis[j] = sanjiao[i-1][j-2]+sanjiao[i-1][j-1]+sanjiao[i-1][j]
    sanjiao.append(lis)


count = 0

for index,i in enumerate(sanjiao[line]):
    if i %2 ==0:
        count+=1
        print(index+1)
        break

if count ==0:
    print('-1')


