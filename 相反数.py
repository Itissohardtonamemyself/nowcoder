# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 23:22:53 2018

@author: LX

相反数

"""

n = input()
nlst = []
for i in n:
    nlst.append(i)
nlst.reverse()
num = ''
for i in nlst:
    num+=i
print(int(n)+int(num))


