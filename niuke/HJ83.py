# -*- coding: utf-8 -*-
# @Time : 2023/4/13 15:19
# @Author : ASUS
# @File : HJ83.py
# @Software: PyCharm
# 4 9
# 5 1 2 6
# 0
# 8
# 2 3


while True:
    flag1 = [-1, -1, -1, -1, -1]
    try:
        row,column =map(int,input().split(' '))

        # print(row,column)
        # 创建数组
        if 1<=row<=9 and 1<=column <=9:
            lis = [[0 for col_1 in range(column)] for row_1 in range(row)]
            # print("111111111111111")
            # print(lis)
            flag1[0] = 0
        # print(flag1[0])

        # 交换两数位置
        y1, x1, y2, x2 = map(int,input().split(' '))
        # print(x1,y1,x2,y2)


        if (0 <= x1<= column-1 and 0<=x2<=column-1 and 0<=y1<=row-1 and 0 <=y2<=row-1):
            lis[y1][x1],lis[y2][x2] = lis[y2][x2],lis[y1][x1]
            flag1[1] =0
        #     print("22222222222")
        # print(flag1[1])


        row_ins = int(input())


        #插入行

        if row<9 and row_ins<=row-1:

            flag1[2]=0
            # print("33333333333")
        # print(flag1[2])
        col_ins = int(input())

        # 插入列

        if column<9 and col_ins<=column-1:
            flag1[3]=0

        #     print("4444444444")
        # print(flag1[3])

        # 查询单元格
        y3, x3 = map(int, input().split(' '))

        if 0 <= y3 <= row-1 and 0 <=x3 <=column-1:
            flag1[4]=0
        #     print("5555555555")
        # print(flag1[4])

        for flag in flag1:
            print(flag)



    except:
        break


