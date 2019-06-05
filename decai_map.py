# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:07:03 2018

@author: LX
"""

ai = list(map(int,input().split()))
N = ai[0]
L = ai[1]
H = ai[2]
alst,a,b,c,d,e = [],[],[],[],[],[]
for i in range(0,N):
    alst.append(list(map(int,input().split())))
for i in range(0,N):
    if alst[i][1]>=H and alst[i][2]>=H:
        a.append(alst[i])
    elif alst[i][1]>=H and alst[i][2]<H and alst[i][2]>=L:
        b.append(alst[i])
    elif alst[i][1]<H and alst[i][2]<H and alst[i][1]>=alst[i][2] and alst[i][1]>=L and alst[i][2]>=L:
        c.append(alst[i])
    elif alst[i][1]>=L and alst[i][2]>=L:
        d.append(alst[i])
    else:
        e.append(alst[i])
a.sort(key=lambda x:(-x[1]-x[2],-x[1],x[0])) 
b.sort(key=lambda x:(-x[1]-x[2],-x[1],x[0]))
c.sort(key=lambda x:(-x[1]-x[2],-x[1],x[0]))
d.sort(key=lambda x:(-x[1]-x[2],-x[1],x[0]))
e.sort(key=lambda x:(-x[1]-x[2],-x[1],x[0]))
liout = a+b+c+d

print(N-len(e))
for i in range(0,len(liout)):
     print(str(liout[i][0])+" "+str(liout[i][1])+" "+str(liout[i][2]))
