# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:04:14 2018

@author: LX

Favorite Color Stripe

"""

#像动态规划问题的最长公共子串问题
n = input()
n = int(n)
m = list(map(int,input().split()[1:]))
l = list(map(int,input().split()[1:]))
con = [[0 for i in range(len(l))] for j in range(len(m)+1)]
for i in range(1,len(m)+1):
    for j in range(len(l)):
        con[i][j]=max(con[i-1][j],con[i][j-1])
        if m[i-1]==l[j]:
            con[i][j]+=1
print(con[len(m)][len(l)-1])


#con,con1,index = 0,0,0
#for i in range(len(m)-1):
#    cur,nex = m[i],m[i+1]
#    for j in range(index,len(l)):
#        if cur==l[j]:
#            con1+=1
#        elif nex==l[j]:
#            con+=con1
#            con1=0
#            index=j
#            break
#cur = m[len(m)-1]
#for j in range(index,len(l)):
#    if cur==l[j]:
#        con+=1
#print(con) 





