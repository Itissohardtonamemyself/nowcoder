# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:47:49 2019

@author: LX

网易 堆棋子

"""

import sys
n = input()
n = int(n)
x = list(map(int,input().split()))
y = list(map(int,input().split()))
def cal(p1,p2,p3,p4):
    return abs(p1-p2)+abs(p3-p4)
res = [sys.maxsize]*n
for i in range(n):
    for j in range(n):
        t=[]
        for k in range(n):
            t.append(cal(x[k],x[i],y[k],y[j]))
        sa = 0
        t.sort()
        for k in range(n):
            sa+=t[k]
            res[k] = min(res[k],sa)
print(' '.join(map(str,res)))