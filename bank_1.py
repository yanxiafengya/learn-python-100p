# -*- coding: utf-8 -*-
# @Time : 2023/4/8 8:45
# @Author : ASUS
# @File : bank_1.py
# @Software: PyCharm
# -*-coding=utf-8-*-

class Banks():
    title = 'Taipei Bank'

    def __init__(self, uname, money) -> None:
        self.name = uname
        self.balance = money

    def get_balance(self):
        return self.balance


hungbank = Banks('hung', 100)
print(hungbank.name.title(), "存款余额是", hungbank.get_balance())