# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:29:59 2018

@author: LX

Student List for Course 

"""

n,m = map(int,input().split())
lst = [[] for i in range(0,m+1)]
for i in range(n):
    temp = input().split()
    tem = list(map(int,temp[2:]))
    for i in tem:
        lst[i].append(temp[0])
for i in range(1,m+1):
    print(i,len(lst[i]))
    lst[i].sort()
    for j in lst[i]:
        print(j)


