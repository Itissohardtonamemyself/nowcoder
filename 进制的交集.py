# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:39:45 2018

@author: LX

进制的交集

"""

def getbf(a3,n):
    out = ''
    a3 = -a3
    while a3>=n:
        out=str(a3%n)+out
        a3 = a3//n
    return "-"+str(a3)+out

def getb(a1,n):
    out = ''
    while a1>=n:
        out=str(a1%n)+out
        a1 = a1//n
    return str(a1)+out
def getshi(b1,n):
    out = 0
    b1 = str(b1)
    for i in range(len(b1)):
        out+=int(b1[i])*(n**(len(b1)-1-i))
    return out
  
t = input()
t = int(t)
for i in range(t):
    a,b = map(int,input().split())
    l1,r1 = map(int,input().split())
    l2,r2 = map(int,input().split())
    if l1>=0:
        ran1 = getshi(l1,a)
    else:
        ran1 = -getshi(abs(l1),a)
    if r1>=0:
        ran2 = getshi(r1,a)
    else:
        ran2 = -getshi(abs(r1),a)
    s1=set([])
    for i in range(ran1,ran2+1):
        if i>=0:
            s1.add(getb(i,a))  
        else:
            s1.add(getbf(i,a)) 
    if l2>=0:
        ran3 = getshi(l2,b)
    else:
        ran3 = -getshi(abs(l2),b)
    if r2>=0:
        ran4 = getshi(r2,b)
    else:
        ran4 = -getshi(abs(r2),b)  
    s2=set([])
    for i in range(ran3,ran4+1):
        if i>=0:
            s2.add(getb(i,b))
        else:
            s2.add(getbf(i,b))
    s3 = s1&s2
    print(len(s3))
        
        