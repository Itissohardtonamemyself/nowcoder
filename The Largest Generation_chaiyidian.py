# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:12:46 2018

@author: LX
"""

def math(a,index):
    temp = []
    for j in lst:
            if j[0]==a:
                conlst[index] = conlst[index] + len(j) - 2
#                con = con - conlst[i]
                temp = list(j)
                lst.remove(j)
    return temp
def loop(lstin,ind):
    tem = []
    for j in range(0,len(lstin)):
        for k in range(2,len(lstin[j])):
            tem.append(math(lstin[j][k],ind))
    return tem

n,m = map(int,input().split())
temlst,conlst,lst,sublst = [],[],[],[]
con = 0
for i in range(0,m):
    lst.append(list(map(int,input().strip().split())))
#backup = list(lst)
for i in range(0,len(lst)):
    if lst[i][0]==1:
        temlst = list(lst[i])
        conlst = [1 for i in range(2,len(lst[i]))]
        del lst[i]
        break
#sumcon = 0
for i in range(2,len(temlst)):
    sublst.append(math(temlst[i],i-2))
while len(lst)>0:
    temlst = list(loop(sublst,con))
    for i in temlst:
        if len(i)==0:
            temlst.remove(i)
    if len(temlst)==0:
        con+=1
    else:
        sublst = list(temlst)
            
            
            