# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:02:27 2018

@author: LX

数组元素循环右移问题

"""


n,m = map(int,input().split())
m = m%n
lst = list(map(str,input().split()))
out = []
for i in range(n-m,n):
    out.append(lst[i])
for i in range(0,n-m):
    out.append(lst[i])
print(' '.join(out))


