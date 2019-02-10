# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:32:58 2018

@author: LX

Spring Outing

"""

#def vote(a):
#    con=0
#    for i in lst:
#        if i.index(a)<i.index(a+1):
#            con+=1
#    return con
#lst,boo = [],True
#
#n,k = map(int,input().split())
#klst = [i for i in range(1,k)]
#for i in range(0,n):
#    lst.append(list(map(int,input().split())))
#if n>2 and k>2:
#    for j in klst:
#        if vote(j)>n//2:
#            boo = False
#            print(j)
#            break
#    if boo:
#        con = 0
#        for i in lst:
#            if i.index(k)<i.index(0):
#                con+=1
#        if con>n//2:
#            print(k)
#        else:
#            print("otaku")
#elif n==2 and k==2:
#    for j in klst:
#        if vote(j)==1:
#            boo = False
#            print(j)
#            break
#    if boo:
#        con = 0
#        for i in lst:
#            if i.index(k)<i.index(0):
#                con+=1
#        if con==1:
#            print(k)
#        else:
#            print("otaku")
#elif n==2 and k==1:
#    if lst[0][0]==1 and lst[1][0]==1:
#        print(1)
#    else:
#        print("otaku")
#elif n==1 and k==1:
#    if lst[0][0]==1:
#        print(1)
#    else:
#        print("otaku")
#else:
#    print("otaku")

#这个题目是不断地做最优比较 选出最优
#import numpy as np
def vote(a):
    global con
    vote = 0
    for i in range(0,n):
        if lst[i][a]<lst[i][con]:
            vote+=1
    if vote>n//2:
        con = a
try:
    while True:
#        lst = np.zeros((1001,1001),dtype=np.int)
        n,k = map(int,input().split())
        lst,con = [[0 for i in range(0,k+1)] for i in range(0,n)],0
        for i in range(0,n):
            tem = list(map(int,input().split()))
            for j in range(0,k+1):
                lst[i][tem[j]] = j     
        for i in range(k,0,-1):
            vote(i)
        if con==0:
            print('otaku')
        else:
            print(con)      
except Exception as e :
    print(e)



#test = np.zeros((2, 3), dtype=np.int)



