# -*- coding: utf-8 -*-
# @Time : 2023/4/13 19:10
# @Author : ASUS
# @File : hj76.py
# @Software: PyCharm

# 1^3=1
#
# 2^3=3+5
#
# 3^3=7+9+11
#
# 4^3=13+15+17+19
# 6^3=31+33+35+37+39+41
# 6(6-1)+1 6(6+1)-1

num = int(input())
lis = []
for num_1 in range(num*(num-1)+1,num*(num+1),2):
    lis.append(str(num_1))
print('+'.join(lis))
