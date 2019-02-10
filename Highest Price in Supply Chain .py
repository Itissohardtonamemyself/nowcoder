# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:33:36 2018

@author: LX

Highest Price in Supply Chain 

"""

#def findindex(org, x):
#    result = []
#    for k,v in enumerate(org): 
#        if v == x:
#            result.append(k)
#    return result
#d = {}
ma=-1
root = -2
n,p,r = map(float,input().split())
n = int(n)
#boo = [True for i in range(n)]
lst = list(map(int,input().split()))
#while boo.count(True)>1:
#    te = []
#    root = -1
#    boo[lst.index(-1)]=True
#    while lst.count(root)>0:
##        root = lst.index(root)
#        temp = findindex(lst,root)
#        for l in temp:
#            if boo[l]:     
#                te.append(l)       
#                boo[l] = False
#                root = l
#                break
#    d[con]=te
#    con+=1
for i in lst:
    con=0
    root = i
    while root!=-1:
        root = lst[root]
        con+=1
    if con>ma:
        ma = con
co = 0
for i in lst:
    con=0
    root = i
    while root!=-1:
        root = lst[root]
        con+=1
    if con==ma:
        co+=1
print("%.2f"%(p*((1+r/100)**ma))+" "+str(co))  




