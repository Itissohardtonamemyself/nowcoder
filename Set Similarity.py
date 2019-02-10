# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:28:33 2018

@author: LX

Set Similarity

"""

n = input() 
n = int(n)
lst = [None for i in range(n)]
for i in range(n):
    tem = set(map(int,input().split()[1:]))
    lst[i] = tem
m = input()
m = int(m)
for i in range(m):
    a,b = map(int,input().split())
    c = lst[a-1]|lst[b-1]
    d = lst[a-1]&lst[b-1]
    print("%.1f"%(len(d)/len(c)*100)+"%")



