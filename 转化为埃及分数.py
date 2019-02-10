# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:39:46 2019

@author: LX

转化为埃及分数
"""

try:
    while True:
        a,b = map(int,input().split('/'))
        while a!=1 and b%a!=0:
            c = b//a+1
            print('1/'+str(c)+'+',end='')
            a = a*c-b
            b = b*c
        print('1/'+str(b//a))
except:
    pass
