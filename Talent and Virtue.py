# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:49:22 2018

@author: LX

Talent and Virtue

"""

n,l,h = map(int,input().split())
lst,a,b,c,d = [],[],[],[],[]
for i in range(n):
    tem = list(map(int,input().split()))
    if tem[1]>=l and tem[2]>=l:
        if tem[1]>=h and tem[2]>=h:
            a.append(tem)
        elif tem[1]>=h and tem[2]<h:
            b.append(tem)
        elif tem[1]<h and tem[2]<h and tem[1]>=tem[2]:
            c.append(tem)
        else:
            d.append(tem)
a.sort(key=lambda x:(-(x[1]+x[2]),-x[1],x[0]))
b.sort(key=lambda x:(-(x[1]+x[2]),-x[1],x[0]))
c.sort(key=lambda x:(-(x[1]+x[2]),-x[1],x[0]))
d.sort(key=lambda x:(-(x[1]+x[2]),-x[1],x[0]))
lst = a+b+c+d
print(len(lst))
for i in lst:
    print(i[0],i[1],i[2])