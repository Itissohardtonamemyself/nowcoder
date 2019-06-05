# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:15:54 2018

@author: LX
"""
n = input()
n = int(n)
lst = []
tem = []
date = ''
for i in range(0,n):
    a = input().strip().split()
    lst.append([a[0]])
    tem = a[1].strip().split('/')
    for j in range(0,len(tem)):
        date = date+tem[j]
    lst[i].append(date)
    date = ''
old = '18140906'
young = '20140906'
count  = 0
mindate = lst[0][1]
mini = 0
maxdate = ''
maxi = 0
for i in range(0,len(lst)):
    if lst[i][1]>=old and lst[i][1]<=young:
        count +=1
        if mindate>=lst[i][1]:
            mindate = lst[i][1]
            mini = i
        if maxdate<=lst[i][1]:
            maxdate = lst[i][1]
            maxi = i
print(str(count)+" "+lst[mini][0]+" "+lst[maxi][0])