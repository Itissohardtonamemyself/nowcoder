# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:48:11 2018

@author: LX

字符串碎片

"""

s = input()
letter,num,sa = '',0,len(s)
for i in s:
    if letter!=i:
       num+=1
       letter=i
print("%.2f"%(sa/num))


