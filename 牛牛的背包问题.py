# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:24:35 2018

@author: LX

牛牛的背包问题

"""


def dfs(su,loc):
    global con
    if su>w:
        return
    if su<=w:
        con+=1
    for i in range(loc,n):
        dfs(su+v[i],i+1)

n,w = map(int,input().split())
v = sorted(map(int,input().split()))
con = 0
if sum(v)<=w:
    print(2**n)
else:
    dfs(0,0)
    print(con)

