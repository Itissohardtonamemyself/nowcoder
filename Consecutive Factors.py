# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:55:47 2018

@author: LX

Consecutive Factors

"""

n = input()
n = int(n)
backup = int(n)
i=2
res,te = [],[]
if n%4!=0 or n%8==0:
    while i**2<=n or n%i==0:
        if n%i==0:
            te.append(i)
            n=n//i 
        else:
            if te:
                res.append(te)
                te = []
                n = int(backup)
        i+=1
else:
    i=3
    while i**2<=n or n%i==0:
        if n%i==0:
            te.append(i)
            n=n//i 
        else:
            if te:
                res.append(te)
                te = []
                n = int(backup)
        i+=1
if te:
    res.append(te)
if backup%4==0 and backup%8!=0:
    res.append([2])
res.sort(key=lambda x:(-x[0]))
out = []
for i in res:
    if len(out)<=len(i):
        out = list(i)
if len(out)>1:
    print(len(out))
    print("*".join(map(str,out)))
elif len(out)==1:
    print(1)
    print(out[0])
else:
    print(1)
    print(backup)