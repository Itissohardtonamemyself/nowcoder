# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:12:50 2018

@author: LX

Find More Coins

"""

def dfs(coins,start,result,j,m):
    for i in range(start,len(coins)):
        if coins[i]<m:
            result[j],flag = coins[i],dfs(coins,i+1,result,j+1,m-coins[i])
            if flag!=j:
                return flag
            result[j]=0
        elif coins[i]==m:
            result[j]=coins[i];
            return j
        else:
            return j-1
    return j-1
n,m = map(int,input().split())
lst = sorted(map(int,input().split()))
result = [0 for i in range(0,n)]
j = dfs(lst,0,result,0,m)
if j<0:
    print("No Solution")
else:
    for i in range(0,j):
        print(str(result[i])+" ",end="")
    print(str(result[j]))
