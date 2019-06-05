# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:47:38 2018

@author: LX

Have Fun with Numbers

"""

lst = ['0','1','2','3','4','5','6','7','8','9']
n = input()
n = int(n)
m = 2*n
nlst,mlst = [],[]
for i in str(n):
    nlst.append(i)
for i in str(m):
    mlst.append(i)
countn,countm = [],[]
for i in lst:
    countn.append(nlst.count(i))
    countm.append(mlst.count(i))
boo = True
for i in range(0,len(lst)):
    if countn[i]!=countm[i] or (countn[i]==0 and countm[i]!=0) or (countn[i]!=0 and countm[i]==0):
        print("No")
        print(str(m))
        boo = False
        break
if boo:
    print("Yes")
    print(str(m))