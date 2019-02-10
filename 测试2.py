# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:16:44 2018

@author: LX


测试2
"""

def c(a,b):
    s1,s2 = 1,1
    for i in range(1,a+1):
        s1*=i
    for i in range(b,b-a,-1):
        s2*=i
    return s2//s1

t = input()
t = int(t)
n,a,b = map(int,input().split())
sa = 0
for i in range(1,n):
    if a>i:
        ta = i
    if b>i:
        tb = i
    t1 = 26**min(ta,tb)*c(min(ta,tb),n)
    if ta>tb:
        t2 = 5**(ta-tb)*c((ta-tb),n-tb)

