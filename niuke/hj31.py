# -*- coding: utf-8 -*-
# @Time : 2023/4/14 16:10
# @Author : ASUS
# @File : hj31.py
# @Software: PyCharm

# 对字符串中的所有单词进行倒排。
# 说明：
# 1、构成单词的字符只有26个大写或小写英文字母；
# 2、非构成单词的字符均视为单词间隔符；
# 3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
# 4、每个单词最长20个字母；

str_in = input()
# print(str_in)

# 创建空集合
fuhao = set()



# 特殊符号
for item in str_in:
    if  not item.isalpha():
        fuhao.add(item)

for item1 in fuhao:

    str_in = ' '.join(str_in.split(item1))


lis_out = str_in.strip().split(' ')
lis_out.reverse()
print(' '.join(lis_out))

