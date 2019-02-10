# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:51:41 2018

@author: LX

Find Coins

"""

n,m = map(int,input().split())
lst = sorted(map(int,input().split()))
start,end = 0,len(lst)-1
while start<end:
    if lst[start]+lst[end]<m:
        start+=1
    elif lst[start]+lst[end]>m:
        end-=1
    else:
        print(str(lst[start])+" "+str(lst[end]))
        break
if start>=end:
    print("No Solution")
#out = []
#for i in range(0,len(lst)-1):
#    boo = False
#    for j in range(i+1,len(lst)):
#        if lst[i]+lst[j]==m:
#            out= [str(lst[i]),str(lst[j])]
#            boo = True
#            break
#    if boo:
#        break
#if out:
#    print(' '.join(out))
#else:
#    print("No Solution")