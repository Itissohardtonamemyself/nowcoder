# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:58:11 2018

@author: LX

To Buy or Not to Buy

"""
boo,con,con1 = True,0,0
nlst,mlst = [],[]
n = input()
m = input()
for i in n:
    nlst.append(i)
for j in m:
    mlst.append(j)
ms = list(set(mlst))
for i in ms:
    if i not in n:
        boo = False
        con+=m.count(i)
    else:
        if n.count(i)<m.count(i):
            boo = False
            con+=m.count(i) - n.count(i)
if boo:
    print("Yes "+str(len(nlst)-len(mlst)))
else:
    print("No "+str(con))