# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:25:55 2018

@author: wentong

function:客似云来

"""
fi = [1,1]+[0 for i in range(2,81)]
for i in range(2,81):
    fi[i]=fi[i-1]+fi[i-2]
try:
    while True:
        s,e = map(int,input().split())
        print(sum(fi[s-1:e]))
except:
    pass
