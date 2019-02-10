# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:08:25 2018

@author: wentong

function:The Dominant Color 

"""


n,m = map(int,input().split())
count,lst,lstin = [],[],[]
for i in range(0,m):
    lstin.append(list(map(str,input().split())))
for i in range(0,m):
    tem = list(lstin[i])
    for j in tem:       
        if j not in lst:
            lst.append(j)
            count.append(1)
        else:
            for k in range(0,len(lst)):
                if lst[k]==j:
                    count[k]+=1
ma = max(count)
index= -1
for i in range(0,len(count)):
    if count[i]==ma:
        index = i
        break
print(lst[index])

