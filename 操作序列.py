# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:06:38 2018

@author: LX

操作序列

"""
from collections import deque
ji,ou = deque([]),deque([])
out = []
n = input()
n = int(n)
lst = list(map(int,input().split()))
if n%2==0:
    for i in range(n):
        if (i+1)%2==0:
            ou.appendleft(lst[i])
        else:
            ji.append(lst[i])
    out = list(ou)+list(ji)
else:
    for i in range(n):
        if (i+1)%2==0:
            ou.append(lst[i])
        else:
            ji.appendleft(lst[i])
    out = list(ji)+list(ou)
print(' '.join(map(str,out)))