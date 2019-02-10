# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:49:47 2018

@author: LX

1003. 我要通过！

"""
def ifconpat(a):
    con1,con2,con3 = 0,0,0
    for i in range(0,a.index('P')):
        if a[i]=='A':
            con1+=1
        else:
            return False
    for i in range(a.index('T')+1,len(a)):
        if a[i]=='A':
            con2+=1
        else:
            return False
    for i in range(a.index('P')+1,a.index('T')):
        if a[i]=='A':
            con3+=1
        else:
            return False
    if con2!=con1*con3:
        return False
    else:
        return True
    
def ifpat(a):
    temp = list(set(a))
    if len(temp)==3 and ('P' in temp) and ('A' in temp) and ('T' in temp):
        return True
    else:
        return False
        
n = input()
n = int(n)
for i in range(0,n):
     m = input()
     tem = []
     for i in m:
         tem.append(i)
     if ifpat(tem) and ifconpat(tem):
         print('YES')
     else:
         print('NO')

