# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:49:49 2018

@author: LX

Linked List Sorting 

"""
#def sou():
#    global start

n,start = map(int,input().split())
if start!=-1:
    lst,lst1 = [None,None]*100001,[]
    for i in range(0,n):
        a,b,c = map(int,input().split())
        lst[a]=[b,c]
    while start!=-1:
        lst1.append([start,lst[start][0]])
        start = lst[start][1]      
    lst1.sort(key = lambda x:(x[1]))
    for i in range(0,len(lst1)-1):
        lst1[i].append(lst1[i+1][0])
    print(str(len(lst1))+" "+"%05d"%lst1[0][0])
    for i in range(0,len(lst1)-1):
        print("%05d"%lst1[i][0]+" "+str(lst1[i][1])+" "+"%05d"%lst1[i][2])
    print("%05d"%lst1[len(lst1)-1][0]+" "+str(lst1[len(lst1)-1][1])+" "+"-1")
else:
    print("0 -1")