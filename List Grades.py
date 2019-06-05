# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:49:12 2018

@author: wentong

function:List Grades

"""

n = input()
n = int(n)
lst = []
for i in range(0,n):
    tem = input().split()
    lst.append([tem[0],tem[1],int(tem[2])])
low , high = map(int,input().split())
lst.sort(key=lambda x:(-x[2]))
out = []
for i in lst:
    if i[2]>=low and i[2]<=high:
        out.append(i[0]+" "+i[1])
if out:
    for i in out:
       print(i)
else:
    print("NONE")