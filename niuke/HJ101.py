# -*- coding: utf-8 -*-
# @Time : 2023/4/14 18:25
# @Author : ASUS
# @File : HJ101.py
# @Software: PyCharm

input()
lis = input().split(' ')
lis_out =list(map(int,lis))
# for i in lis:
#     lis_out.append(int(i))

flag =int(input())
if flag == 0:
    lis_out.sort()
else:
    lis_out.sort(reverse=True)

lis_out = list(map(str,lis_out))
print(' '.join(lis_out))
