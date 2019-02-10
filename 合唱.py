# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:26:05 2018

@author: LX

合唱

"""

dp = [[0 for i in range(2003)] for j in range(2003)]
acc,v = [0 for i in range(2003)],[0 for i in range(2003)]
n = input()
n = int(n)
lst = list(map(int,input().split()))
for i in range(n):
    v[i]=lst[i]
if n<3:
    print(0)
else:
    dp[1][0]=0
    acc[1]=0
    for i in range(2,n):
        acc[i] = acc[i-1]+abs(v[i-1]-v[i-2])
        dp[i][i-1] = acc[i]
        for j in range(0,i-1):
            dp[i][j] = dp[i-1][j] + abs(v[i]-v[i-1])
            dp[i][i-1] = min(dp[i][i-1],dp[i-1][j]+abs(v[i]-v[j]))
    mins = dp[n-1][0]
    for i in range(1,n-1):
        if dp[n-1][i]<mins:
            mins = dp[n-1][i]
    print(mins)

#n=input()
#n = int(n)
#v=list(map(int,input().split()))
#if n<=2:
#    print(0)
#else:
#  dp=[[0]*n for i in range(n)]
#  for i in range(2,n):
#      dp[i][i-1]=dp[i-1][i-2]+abs(v[i-1]-v[i-2])
#  for i in range(2,n):
#      for j in range(i-1):
#          dp[i][j]=dp[i-1][j]+abs(v[i]-v[i-1])
#          dp[i][i-1]=min(dp[i][i-1],dp[i-1][j]+abs(v[i]-v[j]))
#  print(min(dp[n-1][:-1]))