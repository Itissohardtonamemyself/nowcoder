# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:27:15 2018

@author: LX

function:Rational Sum

"""

def findmu(a):
    global ma
    i = 2 
    while ma%a!=0:
        ma = ma * i
        i+=1
def yuefen(q,p):
    j = 2
    temp = []
    while q>1 and j<q:
        if q%j==0:
            q = q//j
            temp.append(j)
        else:  
            j+=1      
    for i in temp:
        if p%i==0:
            p = p//i
    return q,p
                 

n = input()
n = int(n)
lst = list(map(str,input().split()))
zi,mu,tem = [],[],[]
for i in range(0,n):
    tem = list(map(int,lst[i].split("/")))
    zi.append(tem[0])
    mu.append(tem[1])
#找分母
ma = max(mu)
for i in range(0,n):
    findmu(mu[i])
zihe = 0
for i in range(0,n):
    zihe = zi[i]*ma//mu[i] + zihe
if zihe>=0:
    zhen,yu = zihe//ma,zihe%ma
else:
    zhen,yu = -((-zihe)//ma),-((-zihe)%ma)
if yu>2 or yu<-2:
    yu,ma = yuefen(yu,ma)
elif yu==2:
    if ma%2==0:
        yu =1
        ma = ma//2
if zhen!=0 and yu!=0:
    print(str(zhen)+" "+str(yu)+"/"+str(ma))
elif yu==0 and zhen!=0:
    print(str(zhen))
elif yu!=0 and zhen==0:
    print(str(yu)+"/"+str(ma))
else:
    print(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    