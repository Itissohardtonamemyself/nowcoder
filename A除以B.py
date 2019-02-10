# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:25:53 2018

@author: LX

A除以B

"""

a,b = map(str,input().split())
alst = []
for i in a:
    alst.append(i)
b = int(b)
q = ''
i,up = 1,''
if int(alst[0])>=b:
    q = str(int(alst[0])//b)
up = str(int(alst[0])%b)
while i<len(alst):
    num = int(up+alst[i])
    q = q+str(num//b)
    i+=1
    if num%b==0:
        up = ''  
    else:
        up = str(num%b)   
if up=='':
    up = '0'
print(q+" "+up)