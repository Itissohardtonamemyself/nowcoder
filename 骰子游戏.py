# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:17:33 2018

@author: LX

骰子游戏

"""

#fun(n,x) = [fun(n-1,x-1)+fun(n-1,x-2)+fun(n-1,x-3)+fun(n-1,x-4)+fun(n-1,x-5)+fun(n-1,x-6)]//6
#没做出来
def getfen(q,p):
    i=2
    while i**2<=q:
        if q%i and p%i:
            q = q//i
            p = p//i
        i+=1
    return str(q)+"/"+str(p)
n,x = map(int,input().split())
if x==n:
    print(1)
elif x<n or x>6*n:
    print(0)
else:
    dp = [[0 for i in range(150)] for j in range(30)]


