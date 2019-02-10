# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:41:59 2018

@author: LX

有假币

"""

#2，3找一次
def find(a):
    con = 0
    while a>1:
        if a%3==1 or a%3==0:
            a = a - a//3*2
            con+=1
        elif a%3==2:
            a = a//3+1
            con+=1
    return con
try:
    while True:
        n = input()
        n = int(n)
        if n==0:
            break
        else:
            print(find(n))
except:
    pass
 






