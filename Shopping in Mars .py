# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:30:26 2018

@author: LX

Shopping in Mars 

"""

def find(a):
    global m,total
    if len(a)==1 and lst[a[0]]==m:
        print(str(a[0]+1)+"-"+str(a[0]+1))
    if len(a)>1:
        for i in range(1,len(a)):
            low,high = 0,i
            while high-low>1:
                mid = (high+low)//2
                if sum(lst[a[mid]:a[i]+1])>=m:
                    low = mid
                else:
                    high = mid
            sa = sum(lst[low:i+1])
            if sa>=m and sa<total:
                total = sa
            elif sa>=m and sa==total:
                print(str(low+1)+"-"+str(i+1))
        
#        for i in range(0,len(a)-1):
#            con = lst[a[i]]
#            for j in range(i+1,len(a)):
#                if con<=m:
#                    con+=lst[a[j]]
#                if con==m:
#                    print(str(a[i]+1)+"-"+str(a[j]+1))
#                    break
#                if con>m:
#                    break
n,m = map(int,input().split())
total = float('inf')
#减小复杂度
lst = list(map(int,input().split()))
poss = []
tem = []
#res = []
for i in range(0,len(lst)):
    if lst[i]<m:
        tem.append(i)
    elif lst[i]>m:
        poss.append(tem)
        tem = []
    else:
        poss.append(tem)
        poss.append([i])
        tem = []
poss.append(tem)
for i in poss:
    find(i)








#def find(a):
#    global m
#    if len(a)==1 and lst[a[0]]==m:
#        print(str(a[0]+1)+"-"+str(a[0]+1))
#    if len(a)>1:
#        for i in range(0,len(a)-1):
#            con = lst[a[i]]
#            for j in range(i+1,len(a)):
#                if con<=m:
#                    con+=lst[a[j]]
#                if con==m:
#                    print(str(a[i]+1)+"-"+str(a[j]+1))
#                    break
#                if con>m:
#                    break
#n,m = map(int,input().split())
##减小复杂度
#lst = list(map(int,input().split()))
#poss = []
#tem = []
#for i in range(0,len(lst)):
#    if lst[i]<m:
#        tem.append(i)
#    elif lst[i]>m:
#        poss.append(tem)
#        tem = []
#    else:
#        poss.append(tem)
#        poss.append([i])
#        tem = []
#poss.append(tem)
#for i in poss:
#    find(i)