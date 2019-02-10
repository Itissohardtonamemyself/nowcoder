jav# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:24:36 2018

@author: wentong

function:
了解到了 深拷贝 b = a .则a,b共同使用一个数据地址
浅拷贝b = list(a) 则a改变 b不受影响

"""
import sys
def dfs(fro,cur,des,adj,time):
    global minTime,send,collect,result
    visited[cur] = True
    path.append(cur)
    time += adj[fro][cur]
    if cur == des:
        s,c = 0,0
        for i in range(1,len(path)):
            j = path[i]
            if ci[j]>cmax//2:
                c += ci[j]-cmax//2
            elif ci[j]<cmax//2:
                if c>(cmax//2)-ci[j]:
                    c -= cmax//2 - c[j]
                else:
                    s += (cmax//2)-ci[j]-c
                    c = 0
        if time==minTime:
            if (s<send or (s==send and c<collect)):
                minTime = time
                result = list(path)
                send = s
                collect = c
        elif time<minTime:
            minTime = time
            result = list(path)
            send = s
            collect = c
    else:
        for i in range(0,n):
            if visited[i]==False and adj[cur][i]!=0:
                dfs(cur,i,des,adj,time)
    path.pop()
    visited[cur] = False

cmax,n,sp,m = map(int,input().strip().split())
n = n+1
path,result = [],[]
minTime = sys.maxsize
send = 0
collect = 0
visited = [0 for i in range(0,n)]
ci = [0]
ci.extend(list(map(int,input().strip().split())))
adj = [[0 for i in range(0,n)] for i in range(0,n)]
tem = []
for i in range(0,m):
    tem = list(map(int,input().strip().split()))
    adj[tem[0]][tem[1]] = tem[2]
    adj[tem[1]][tem[0]] = tem[2]
dfs(0,0,sp,adj,0)
print(str(send)+" ",end='')
for i in range(0,len(result)-1):
    print(str(result[i])+"->",end='')
print(str(result[-1])+" ",end = '')
print(collect)





