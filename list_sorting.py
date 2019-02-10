# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:31:45 2018

@author: LX

function:List Sorting

"""
n,c = map(int,input().split())
lst = []
for i in range(0,n):
    lst.append(list(map(str,input().split())))
if c == 1:
    lst.sort(key=lambda x:(x[0]))
elif c==2:
    lst.sort(key=lambda x:(x[1],x[0]))
else:
    lst.sort(key=lambda x:(x[2],x[0]))
for i in range(0,len(lst)):
    print(" ".join(lst[i]))
