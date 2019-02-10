# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:18:03 2018

@author: LX

Sort with Swap(0,*) 

"""
#思路就是以零为基准进行置换
lst = list(map(int,input().split()[1:]))
num,res = 0,0
for i in range(0,len(lst)):
    if lst[i]!=0 and lst[i]!=i:
        num+=1
while num:
    if lst[0]==0:
        for j in range(1,len(lst)):
            if lst[j]!=j:
                te1,te2 =  lst[0],lst[j]
                lst[0],lst[j] = te2,te1
                res+=1
                break
    while lst[0]!=0:
        te1,te2 = lst[lst[0]],lst[0]
        lst[lst[0]],lst[0] = te2,te1
        res+=1
        num-=1
print(res)