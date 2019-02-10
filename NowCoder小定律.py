# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:15:03 2018

@author: LX

NowCoder小定律

"""

def math(m):
    tem = m*m+m+41
    t = int(pow(tem,0.5))
    for j in range(2,t+1):
        if tem%j==0:
            return False
    return True
def domath(a,b):
    for n in range(a,b+1):
        if math(n)==False:
            return False
    return True 

try:
    while True:
        x,y = map(int,input().split())
        if x==0 and y==0:
            break
        if domath(x,y):
            print("OK")
        else:
            print("Sorry")
except:
    pass
