# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:32:48 2018

@author: LX

"""

def cal(a1,a2,b):
    st = '%d'%(a1/a2)+"."
    a1 = a1%a2*10
    while b:
        st = st + "%d"%(a1/a2)
        a1 = a1%a2*10
        b-=1
    return st
try:
    while True:
        a,b,c = map(int,input().split())
        print(cal(a,b,c))
except:
    pass