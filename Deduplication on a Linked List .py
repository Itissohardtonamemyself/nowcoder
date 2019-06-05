# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:21:29 2018

@author: LX

Deduplication on a Linked List 

"""

#def pe(a):
#    if a in tem:
#        tem.remove(a)
#        return True
#    else:
#        return False
#def po(a):
#    for k in lstran:
#        if abs(int(k[1]))==a:
#            return k



lstin,lstran,lsto,lstp = [],[],[],[]
start,n = map(str,input().split())
n = int(n)
for i in range(0,n):   
    lstin.append(list(map(int,input().split())))
while lstin:
    for i in lstin:
        if i[0]==start:
            lstran.append(i)
            start = i[2]
            lstin.remove(i)
            continue
tem = []
for i in lstran:
    if abs(int(i[1])) not in tem:
        tem.append(abs(int(i[1])))
        lsto.append(i)
    else:
        lstp.append(i)
for i in range(0,len(lsto)-1):
    lsto[i][2] = lsto[i+1][0]
for i in range(0,len(lstp)-1):
    lstp[i][2] = lstp[i+1][0]
lstp[len(lstp)-1][2] = '-1'
lsto[len(lsto)-1][2] = '-1'
lstout = lsto+lstp
for i in lstout:
    print(' '.join(i))
#tem = []
#for i in lstran:
#    tem.append(abs(int(i[1])))
#tem = list(set(tem))
#temp = []
#for i in lstran:
#    if pe(abs(int(i[1]))):
#        temp.append(abs(int(i[1])))
#for i in temp:
#    lsto.append(po(i))
#for i in lsto:
#    lstran.remove(i)
#for i in range(0,len(lstran)-1):
#    lstran[i][2] = lstran[i+1][0]
#for i in range(0,len(lsto)-1):
#    lsto[i][2] = lsto[i+1][0]
#lstran[len(lstran)-1][2] = '-1'
#lsto[len(lsto)-1][2] = '-1'
#lstout = lsto+lstran
#for i in lstout:
#    print(' '.join(i))


