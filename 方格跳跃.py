# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:12:36 2018

@author: LX

方格跳跃

"""

maxn = 2005
dis,px,py = [0 for i in range(maxn*maxn)],[0 for i in range(maxn*maxn)],[0 for i in range(maxn*maxn)]
a = [[0 for i in range(maxn)] for j in range(maxn)]
h,w,d = map(int,input().split())
for i in range(1,w+1):
    t = list(map(int,input().split()))
    for j in range(1,h+1):
        a[j][i] = t[j-1]
        px[a[j][i]],py[a[j][i]] = j,i
for i in range(d+1,h*w+1):
    dis[i] = dis[i-d]+abs(px[i]-px[i-d])+abs(py[i]-py[i-d])
q = input()
q = int(q)
for i in range(q):
    l,r = map(int,input().split())
    print(dis[r]-dis[l])

