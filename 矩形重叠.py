# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:00:20 2018

@author: LX

矩形重叠

"""

n = input()
n = int(n)
x1 = list(map(int,input().split()))
y1 = list(map(int,input().split()))
x2 = list(map(int,input().split()))
y2 = list(map(int,input().split()))
con = 0
for x in x1+x2:
    for y in y1+y2:
        count = 0
        for i in range(n):
            if x>=x1[i] and y>=y1[i] and x1<x2[i] and y<y2[i]:
                count+=1
        con = max(con,count)
print(con)
#x1ma,y1ma,x2mi,y2mi = x1[0],y1[0],x2[0],y2[0]
#for i in range(1,n):
#    if x1[i]<x2mi and x1ma<=x1[i] and y1[i]<y2mi and y1ma<=y1[i]:
#        x1ma = x1[i]
#        y1ma = y1[i]
#    if x1ma<x2[i] and x2mi>=x2[i]and y1ma<y2[i] and y2mi>=y2[i]:
#        x2mi = x2[i]
#        y2mi = y2[i]
#con = 0
#for i in range(n):
#    if x1[i]<=x1ma and y1[i]<=y1ma and x2mi<=x2[i] and y2mi<=y2[i]:
#        con+=1
#if con:
#    print(con)
#else:
#    print(1)
