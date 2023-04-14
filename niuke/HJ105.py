# -*- coding: utf-8 -*-
# @Time : 2023/4/12 20:15
# @Author : ASUS
# @File : HJ105.py
# @Software: PyCharm
# 输入 n 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
# 本题有多组输入数据，输入到文件末尾。
lis =[]
fushu = 0
zhengshu =[]
sumnum=0
while True:
    try:
        lis.append(int(input()))
    except:
        for i in lis:
            if i <0:
                fushu+=1
            elif i >0:
                zhengshu.append(i)

        if len(zhengshu) == 0:
            avgnum = 0.0
        else:
            for num in zhengshu:
                sumnum += int(num)
            avgnum =  round(sumnum/len(zhengshu),1)
        break
print(fushu)
print(avgnum)
