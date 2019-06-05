# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:27:24 2018

@author: LX

Path of Equal Weight


"""
def dfs(i,cur,wei,path):
    path.append(weight[i])
    cur +=weight[i]
    if not tree[i] and cur == wei:
        print(' '.join(list(map(str,path))))
    if tree[i]:
        for k in tree[i]:
            dfs(k,cur,wei,path)
    path.pop()
n,m,w = map(int,input().split())
weight = list(map(int,input().split()))
tree = [None]*n
for i in range(0,m):
    tem = list(map(int,input().split()))
    temp = list(tem[2:])
    temp.sort(key=lambda x:(-weight[x]))
    tree[tem[0]]=list(temp)
path = []
dfs(0,0,w,path)
    