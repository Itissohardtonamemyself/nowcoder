# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:19:15 2018

@author: LX

Palindromic Number

"""

def ise(a):
    t1,te = [],''
    for i in a:
        t1.append(i)
    t1.reverse()
    for i in t1:
        te+=i
    if te==a:
        return True
    else:
        return False
n,k = map(int,input().split())
num = int(k)
while k:
    n1,n2 = int(n),[]
    n = str(n)
    for i in n:
        n2.append(i)
    n2.reverse()
    ns = ''
    for i in n2:
        ns+=i
    ns = int(ns)
    n = ns+n1
    k-=1
    if ise(str(n)):
        break
print(n)
print(num-k)