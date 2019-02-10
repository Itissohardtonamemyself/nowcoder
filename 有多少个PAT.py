# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:37:19 2018

@author: 有多少个PAT

function：字符串APPAPT中包含了两个单词“PAT”，其中第一个PAT是第2位(P),第4位(A),第6位(T)；第二个PAT是第3位(P),第4位(A),第6位(T)。

现给定字符串，问一共可以形成多少个PAT？

"""

#def dele(a,lb):
#    index = 0
#    lst = []
#    lst = list(lb)
#    for i in range(0,len(lst)):
#        if lst[i]>a:
#            index = i
#            break
#    del lst[:index]
#    return lst
    
conp,conpa,conall = 0,0,0
s = input()
for i in s:
    if i=='P':
        conp = conp+1
    elif i=='A':
        conpa = conpa + conp
    else:
        conall = conall+conpa
print(conall%1000000007)


#lsts = []
#for i in s:
#    lsts.append(i)
#plst,alst,tlst = [],[],[]
#for i in range(0,len(lsts)):
#    if lsts[i]=='P':
#        plst.append(i)
#        break
#for i in range(plst[0]+1,len(lsts)):
#    if lsts[i]=='P':
#        plst.append(i)
#    if lsts[i]=='A':
#        alst.append(i)
#        break
#for i in range(alst[0]+1,len(lsts)):
#    if lsts[i]=='P':
#        plst.append(i)
#    if lsts[i]=='A':
#        alst.append(i)
#    if lsts[i]=='T':
#        tlst.append(i)
#con = len(alst)*len(tlst)
#tema,temt = 0,0
#
#for i in range(1,len(plst)):
#    alst = dele(plst[i],alst)
#    if len(alst) == 0:
#        break
#    if tema!=len(alst):
#        tema = len(alst)
#    else:
#        tema = 0
#    for j in range(0,len(alst)):
#        tlst = dele(alst[j],tlst)
#        if len(tlst) == 0:
#            break
#        if temt!=len(tlst):
#            temt = len(tlst)
#        else:
#            temt = 0
#        con = con + tema*temt
#print(con%1000000007)