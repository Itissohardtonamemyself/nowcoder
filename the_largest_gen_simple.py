# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:21:38 2018

@author: 1
"""
def loopone(lstin):
    global con
    tem = []
    for i in range(0,len(lstin)):
        for j in range(2,len(lstin[i])):
            for k in lst:
                if k[0] == lstin[i][j]:
                    con = con+k[1]
                    tem.append(k)
                    lst.remove(k)
    return tem

def loop(lstin):
    global con
    tem = []
    for j in range(2,len(lstin)):
        for k in lst:
            if k[0] == lstin[j]:
                con = con+k[1]
                tem.append(k)
                lst.remove(k)
    return tem

n,m = map(int,input().split())
temlst,conlst,lst,sublst,gencon = [],[],[],[],[1]
con = 0
for i in range(0,m):
    lst.append(list(map(int,input().strip().split())))
for i in range(0,len(lst)):
    if lst[i][0]==1:
        temlst = list(lst[i])
        con = con + lst[i][1] 
        del lst[i]
        break
gencon.append(con)
con = 0
index = 0
temlst = loop(temlst)
gencon.append(con)
con = 0
conlst = list(temlst)
while len(lst)>0:
    if isinstance(conlst[0], list) and len(conlst)>0:
        conlst = loopone(conlst)
        gencon.append(con)
        con = 0
    elif isinstance(conlst[0], int) and len(conlst)>0:
        conlst = loop(conlst)
        gencon.append(con)
        con = 0
    elif len(conlst)==0:
        break
ma = max(gencon)
mindex = 0
for i in range(0,len(gencon)):
    if gencon[i]==ma:
        mindex = i+1
print(str(ma)+" "+str(mindex))