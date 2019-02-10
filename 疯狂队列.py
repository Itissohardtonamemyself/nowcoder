# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:07:17 2018

@author: LX

疯狂队列

"""

n = input()
lst = sorted(map(int,input().split()))
ma = -1
index = -1
for i in range(n-1):
    if lst[i+1]-lst[i]>ma:
        ma = lst[i+1]-lst[i]
        index = i
mi,ma = lst[:index+1],lst[index+1:]
ma.reverse()
ran = min(len(mi),len(ma))
out = []
if len(mi)>len(ma):
    for i in range(ran):
        out.append(mi[i])
        out.append(ma[i])
    out.append(mi[ran+1])
