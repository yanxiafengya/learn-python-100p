# -*- coding: utf-8 -*-
# @Time : 2023/4/13 19:21
# @Author : ASUS
# @File : HJ73.py
# @Software: PyCharm

import datetime

while True:
    try:
        y, m, d = map(int, input().split())
        d = datetime.date(y, m, d)  # 录入日期

        print(d.strftime("%j").strip())  # 指定输出一年内的天数并且去掉左边的0
    except:
        break