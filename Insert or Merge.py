# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 23:12:34 2018

@author: LX

Insert or Merge

"""
def merge(a):
    if len(a)==1:
        return
    con = len(a)//2
    temp =[]
    telst = []
    for i in range(0,con):
        tem = a[2*i]+a[2*i+1]
        tem.sort()
        telst.append(tem)
        temp = temp+tem
    for i in a[2*(con-1)+2:]:
        temp = temp+i
    if a[2*(con-1)+2:]:
        telst.extend(a[2*(con-1)+2:])
    merger.append(temp)
    merge(telst)

def insert(a):
    tem = []
    for i in range(0,len(a)):
        tem = tem + [a[i]]
        tem.sort()
        if tem+a[i+1:] not in inser:
            inser.append(tem+a[i+1:]) 
inser,merger = [],[]
n = input()
n = int(n)
lst = list(map(int,input().split()))
b = list(map(int,input().split()))
insert(lst)
merge([[i] for i in lst])
if b in inser:
    print("Insertion Sort")
    print(' '.join(map(str,inser[inser.index(b)+1])))
else:
    print("Merge Sort")
    print(' '.join(map(str,merger[merger.index(b)+1])))

