# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:23:37 2019

@author: LX

小易喜欢的书列
"""

mod = 1000000007
n,k = map(int,input().split())
state = [[0 for i in range(k+1)] for j in range(n+1)]
for i in range(1,k+1):
    state[1][i] = 1
for i in range(1,n):
    t = sum(state[i])
    for j in range(1,k+1):
        tt = sum(state[i][2*j::j])
        state[i+1][j] = (t-tt)%mod
print(sum(state[n])%mod)