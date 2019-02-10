# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 09:21:02 2018

@author: LX

Sharing

"""

start1,start2,n = map(int,input().split())
lst,lst1 = [None]*100001,set([])
boo = True
#boo = [False,False]*n
for i in range(n):
    tem = list(input().split())
    lst[int(tem[0])] = int(tem[2])
while start1!=-1:
    lst1.add(start1)
    start1 = lst[start1]
while start2!=-1:
    temp = start2
    if temp in lst1:
        boo = False
        print("%5d"%temp)
        break
    else:
        start2 = lst[start2]
#for i in lst1:
#    if i in lst2:
#        boo = False
#        print("%5d"%i[0])
#        break
if boo:
    print("-1")