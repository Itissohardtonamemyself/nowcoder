# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:07:24 2018

@author: LX

Reversible Primes

"""

def reverse(a,b):
    nlst=[]
    while a>=b:
        nlst += [a%b]
        a=a//b
    nlst+=[a]
    out = 0
    for i in range(len(nlst)-1,-1,-1):
        out+=nlst[len(nlst)-1-i]*(b**i)
    return out
def isp(a):
    b = 3
    if a<=1:
        return False
    elif a==2:
        return True
    elif a%2==0:
        return False
    else:
        while b**2<a:
            if a%b==0:
                return False
            b+=2
        return True
try:
    while True:
        n,d = map(int,input().split())
        if isp(n) and isp(reverse(n,d)):
            print('Yes')
        else:
            print('No')      
except:
    pass

