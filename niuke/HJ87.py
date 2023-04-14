# -*- coding: utf-8 -*-
# @Time : 2023/4/13 9:32
# @Author : ASUS
# @File : HJ87.py
# @Software: PyCharm

pingfen ={
    90: 'VERY_SECURE',
    80: 'SECURE',
    70: 'VERY_STRONG',
    60: 'STRONG',
    50: 'AVERAGE',
    25: 'WEAK',
    0:  'VERY_WEAK',
}

password = input()
score = 0

# 密码长度
# 一、密码长度:
# 5 分: 小于等于4 个字符
# 10 分: 5 到7 字符
# 25 分: 大于等于8 个字符
def password_len(password,score):
    length = len(password)
    if length<=4:
        score +=5
    elif length<=7:
        score +=10
    else:
        score +=25
    return score

# 二、字母:
# 0 分: 没有字母
# 10 分: 密码里的字母全都是小（大）写字母
# 20 分: 密码里的字母符合”大小写混合“
def zimu(password,score):
    zimu_count = 0
    daxiaoxieflag =0

    for item in password:
        if item.isalpha():
            zimu_count+=1
    if (zimu_count>0 and(password.islower() or password.isupper())):
        score +=10
    elif not (password.isupper() or password.islower()):
        score +=20
        daxiaoxieflag = 1
    return score,zimu_count,daxiaoxieflag

# 三、数字:
# 0 分: 没有数字
# 10 分: 1 个数字
# 20 分: 大于1 个数字

def shuzi(password:str,score:int):
    shuzi_num = 0
    for i in password:
        if i.isdigit():
            shuzi_num +=1
    if shuzi_num==1:
        score +=10
    elif shuzi_num >1:
        score +=20
    return score,shuzi_num

# 四、符号:
# 0 分: 没有符号
# 10 分: 1 个符号
# 25 分: 大于1 个符号
def fuhao(password:str,score:int):
    teshufuhao ='!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'
    fuhaocount = 0
    for item in password:
        if item in teshufuhao:
            fuhaocount +=1
    if fuhaocount==1:
        score+=10
    elif fuhaocount>1:
        score+=25
    return score,fuhaocount

# 长度分数
score = password_len(password,score)
# print('------')
# print(score)
score,zimu_count,daxiaoxieflag = zimu(password,score)
# print(score)
score,shuzi_num=shuzi(password,score)
# print(score)
score,fuhaocount = fuhao(password,score)
# print(score)
if daxiaoxieflag>0 and shuzi_num>0 and fuhaocount>0:
    score+=5

elif zimu_count>0 and shuzi_num>0 and fuhaocount >0:
    score +=3
elif zimu_count>0 and shuzi_num>0 and fuhaocount ==0:
    score += 2
for key in pingfen.keys():
    if score >= int(key):
        final_pingfen = pingfen[key]
        break
    # print(key,pingfen[key])

print(final_pingfen)