# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:50:57 2018

@author: 1

选大王

"""
#我这个写法没有用任何算法，复杂度很大，不推荐
#def ii(a):
#    for i in range(a+1,len(lst)):
#        if lst[i]:
#            return i
#    for i in range(0,a):
#        if lst[i]:
#            return i
#
#def pr():
#    for i in range(0,n):
#        if lst[i]:
#            return i+1
#
#try:
#    while True:   
#        n,m = map(int,input().split())
#        lst = [True for i in range(0,n)]
#        con = 0
#        start = 0
#        while lst.count(True)>1:
#            if con+start>=len(lst):
#                index = con+start-len(lst)
#            else:
#                index = con+start
#            if m-1+start>=len(lst):
#                end = m-1+start-len(lst)
#            else:
#                end = m-1+start
#            if lst[index] and index==end:
#                lst[index]=False
#                index = int(ii(index))
#                if index<len(lst):
#                    start = index
#                else:
#                    start = 0
#                con = 0
#            elif lst[index]:
#                    con+=1
#            else:
#                start+=1
#        out = pr()
#        print(out)
#except:
#    pass



try:
    while True:
        n,m = map(int,input().split())
        num = 0
        for i in range(2,n+1):
            num = (num+m)%i
        num+=1
        print(num)
        
except:
    pass

