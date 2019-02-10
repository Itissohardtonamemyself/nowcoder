# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:54:07 2019

@author: LX

lucky string

"""

ls = set([])
def string(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)+1):
            ls.append(x[i:j])
f = [1,2]+[0]*8
for i in range(2,10):
    f[i] = f[i-1]+f[i-2]
s = input()
string(s)
o = []
for i in ls:
    if len(set(i)) in f:
        o.append(i)
o.sort()
for i in o:
    print(i)