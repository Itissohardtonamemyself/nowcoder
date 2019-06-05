# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:12:49 2018

@author: LX

Perfect Sequence

"""

#n,p = map(int,input().split())
#lst = sorted(map(int,input().split()))
#low,high = 0,n-1
#while lst[low]*p<lst[high]:
#    mid = (low+high)//2
#    if lst[mid]*p<lst[high] and lst[low]*p>=lst[mid]:
#        high-=1
#    elif lst[mid]*p>=lst[high] and lst[low]*p<lst[mid]:
#        low+=1
#    else:
#        te1 = lst[high]-lst[mid]*p
#        te2 = lst[mid]-lst[low]*p
#        if te1>0 and te2>0 and te1>te2:
#            high-=1
#        elif te1>0 and te2>0 and te1<=te2:
#            low+=1
#        elif te1<=0 and te2<=0 and te1>te2:
#            low+=1
#        elif te1<=0 and te2<=0 and te1<=te2:
#            high-=1
#print(high-low+1)

#def panduan(a,b,mi):
#    if lst[a]-mi>mi-lst[b]:
#        return True
#    elif lst[a]-mi<mi-lst[b]:
#        return False
#    else:
#        a-=1
#        b+=1
#        panduan(a,b,mi)
#n,p = map(int,input().split())
#lst = sorted(map(int,input().split()))
#low,high = 0,n-1
#while lst[low]*p<lst[high]:
#    mid  = (lst[high]+lst[low])/2
#    if lst[high]-mid>mid-lst[low]:
#        high-=1
#    else:
#        if panduan(high,low,mid):
#            high-=1
#        else:
#            low+=1
#print(high-low+1)

n,p = map(int,input().split())
lst = sorted(map(int,input().split()))
out = 0
for i in range(n):
    while i+out<n and lst[i+out]<=lst[i]*p:
        out+=1
print(out)


