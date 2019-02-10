# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:00:27 2018

@author: LX

分数运算

"""

def yuefen(a,b):
    i = 2
    while abs(a)>1 and abs(b)>1:
        if a%i==0 and b%i==0:
            a=a//i
            b=b//i
        else:
            i+=1
            if (i==abs(a) or i==abs(b)) and (a%i!=0 or b%i!=0):
                return a,b
    return a,b
try:
    while True:      
        tem = list(map(str,input().split()))
        zi1,mu1 = map(int,tem[0].split('/'))
        zi2,mu2 = map(int,tem[1].split('/'))
        if tem[2]=='+':
            zi = zi1*mu2+zi2*mu1
            mu = mu1*mu2
        elif tem[2]=='-':
            zi = zi1*mu2-zi2*mu1
            mu = mu1*mu2
        elif tem[2]=='*':
            zi = zi1*zi2
            mu = mu1*mu2
        elif tem[2]=='/':
            zi = zi1*mu2
            mu = mu1*zi2
        out1,out2 = yuefen(zi,mu)
        print(str(out1)+'/'+str(out2))
except:
    pass

