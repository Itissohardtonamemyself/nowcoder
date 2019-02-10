# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:20:07 2018

@author: LX

蟠桃记

"""

def cal(a):
    con = 1
    while a>1:
        con = 2*(con+1)
        a-=1
    return con
try:
    while True:
        n = input()
        n = int(n)
        if n:
            print(cal(n))
        else:           
            break
except:
    pass