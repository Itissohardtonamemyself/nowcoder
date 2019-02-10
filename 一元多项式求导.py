# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 09:41:41 2018

@author: LX

一元多项式求导

"""


n = list(map(int,input().split()))
if n[len(n)-1]==0:
    n.pop()
    n.pop()
for i in range(0,len(n)//2):
    n[2*i] = n[2*i]*n[2*i+1]
    n[2*i+1]-=1
out = list(map(str,n))
if out:
    print(' '.join(out))
else:
    print("0 0")