# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:21:27 2018

@author: LX

function:A+B Format

"""

a,b = map(int,input().split())
c = str(a + b)
lsc= []
for i in c:
    lsc.append(i)
cnt = 0
lsout = []
for i in range(len(lsc)-1,-1,-1):
    if lsc[i]>='0' and lsc[i]<='9':
       cnt+=1
if cnt>6:
   lsout = lsc[:len(lsc)-6]+[","]+lsc[len(lsc)-6:len(lsc)-3]+[',']+lsc[len(lsc)-3:]     
elif cnt>3:
    lsout = lsc[:len(lsc)-3]+[',']+lsc[len(lsc)-3:]   
out = ''
for i in lsout:
    out = out + i
if out!='':
    print(out)
else:
    for i in lsc:
        out = out + i
    print(out)


