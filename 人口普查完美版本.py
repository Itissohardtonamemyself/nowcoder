# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:58:22 2018

@author: LX


"""

n = input()
n = int(n)
lst = []
tem = []
for i in range(0,n):
    tem = []
    tem = input().strip().split()
    lst.append([tem[0]])
    tem1 = tem[1].split("/")
    time = ''
    for j in range(0,len(tem1)):
        time = time + tem1[j]
    lst[i].append(time)

start = '18140906'
end = '20140906'
maxind = 0
maxstr = ''
minind = 0
minstr = lst[0][1]
count = 0

for j in range(0,len(lst)):
    if lst[j][1]<=end and lst[j][1]>=start:
        count+=1
        if maxstr<lst[j][1]:
            maxstr = lst[j][1]
            maxind = j
        if minstr>lst[j][1]:
            minstr = lst[j][1]
            minind = j     
print(str(count)+" "+lst[minind][0]+" "+lst[maxind][0])