# -*- coding: utf-8 -*-
# @Time : 2023/4/13 9:05
# @Author : ASUS
# @File : HJ94.py
# @Software: PyCharm

# 请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。

# 第一行输入候选人的人数n，第二行输入n个候选人的名字（均为大写字母的字符串），第三行输入投票人的人数，第四行输入投票。

# 按照输入的顺序，每行输出候选人的名字和得票数量（以" : "隔开，注：英文冒号左右两边都有一个空格！），最后一行输出不合法的票数，格式为"Invalid : "+不合法的票数。

hxr_num = int(input())
dict_piaoshu = {}
Invalid = 0
hxr_name = input().split(' ')
for name in hxr_name:
    dict_piaoshu[name] = 0
toupiaonum = input()
toupiao = input().split()
for piao in toupiao:
    if piao in dict_piaoshu.keys():
        dict_piaoshu[piao] +=1
    else:
        Invalid +=1
for item in dict_piaoshu.items():
    print(str(item[0])+' : ' +str(item[1]))
print('Invalid : '+str(Invalid))