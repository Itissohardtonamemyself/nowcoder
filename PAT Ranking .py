# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:51:00 2018

@author: LX

PAT Ranking 

"""

n = input()
n = int(n)
lst = []
for i in range(0,n):
    t = []
    tem = input()
    tem = int(tem)
    for j in range(0,tem):
        temp = list(map(str,input().split()))
        t.append([temp[0],int(temp[1]),str(i+1)])
    t.sort(key = lambda x:(-x[1],x[0]))
    con,con1= 1,1
    t[0].append(str(1))
    for i in range(0,len(t)-1):
        if t[i][1]!=t[i+1][1]:
            con+=con1
            con1 = 1
            t[i+1].append(str(con))
        else:
            con1+=1
            t[i+1].append(str(con))
    lst.extend(t)
lst.sort(key = lambda x:(-x[1],x[0]))
con,con1= 1,1
lst[0].append(str(1))
for i in range(0,len(lst)-1):
    if lst[i][1]!=lst[i+1][1]:
        con+=con1
        con1 = 1
        lst[i+1].append(str(con))
    else:
        con1+=1
        lst[i+1].append(str(con))
print(len(lst))
for i in lst:
    print(i[0]+" "+i[4]+" "+i[2]+" "+i[3])

