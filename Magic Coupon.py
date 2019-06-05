# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:57:46 2018

@author: wentong

function:Magic Coupon

"""

#简单来说 就是正数乘正数，负数乘负数
n = input()
n = int(n)
lst1 = list(map(int,input().split()))
lst1P,lst1N = [],[]
for i in lst1:
    if i>=0:
        lst1P.append(i)
    else:
        lst1N.append(i)
m = input()
m = int(m)
lst2 = list(map(int,input().split()))
lst2P,lst2N = [],[]
for i in lst2:
    if i>=0:
        lst2P.append(i)
    else:
        lst2N.append(i)
if lst1P:
    lst1P.sort()
    lst1P.reverse()
if lst1N:   
    lst1N.sort()
if lst2P:
    lst2P.sort()
    lst2P.reverse()
if lst2N:
    lst2N.sort()
su = 0
miP = min(len(lst1P),len(lst2P))
miN = min(len(lst1N),len(lst2N))
for i in range(0,miP):
    su+=lst1P[i]*lst2P[i]
for i in range(0,miN):
    su+=lst1N[i]*lst2N[i]   
print(su)


