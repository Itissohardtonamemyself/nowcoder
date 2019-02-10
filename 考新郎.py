# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 10:45:50 2018

@author: LX

考新郎

"""

def cal(a,b):
    con1,con2 = 1,1
    for i in range(1,b+1):
        con1 = con1*i
    for i in range(a,a-b,-1):
        con2 = con2*i
    return con2//con1*f[b] 
f = [0,0,1]+[0 for i in range(3,21)]
for i in range(3,21):
    f[i] = (i-1)*(f[i-1]+f[i-2])
try:
    while True:       
        n,m = map(int,input().split())
        print(cal(n,m))     
except:
    pass

