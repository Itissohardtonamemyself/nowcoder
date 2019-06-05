# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:16:35 2018

@author: wentong

function:Emergency

"""

#def find(k,a,q):
#     temcost,temem,con,key = 0,0,0,False
#     while True in boo:
#        for i in range(0,len(city[k])):
#            if city[k][i]!=0 and k!=c2:           
#                temcost = temcost+city[k][i]
#                temem = temem + resteam[k]
#                boo[k] = False
#                a = list(a) + [a[q].append(i)]
#            elif city[k][i]!=0 and k==c2:           
#                    temcost = temcost+city[k][i]
#                    temem = temem + resteam[k]
#                    boo[k]=False
#            else:
#                con+=1
#                if con>=n+1:
#                    key = True
#                    break
#     return a,key
#
#def findroad(a):
#    for q in range(0,len(a)):
#        for k in a[q]:
#           temres,key = find(k,a,q)
#           if key:
#               continue
#           else:      
#               boo = [True for i in range(0,n)]
#               findroad(temres)
#    return a
def dijkstra(citys,reasue,N,start,end):
    dist = [sys.maxsize for i in range(0,N)]
    visited = [False for i in range(0,N)]
    gt = [0 for i in range(0,N)]
    sps = [0 for i in range(0,N)]
    
    dist[start],gt[start],sps[start] = 0,reasue[start],1
    for i in range(0,N):
        minDist = sys.maxsize
        for j in range(0,N):
            if visited[j]==False and dist[j]<minDist:
                minDist = dist[j]
                k = j
        visited[k] = True
        for j in range(0,N):
            if visited[j]==False and citys[k][j]<sys.maxsize:
                tempDist = dist[k] + citys[k][j]
                if tempDist<dist[j]:
                    dist[j] = tempDist
                    sps[j] = 1
                    gt[j] = gt[k] + reasue[j]
                elif tempDist==dist[j]:
                    sps[j] +=1
                    gt[j] = max(gt[j],gt[k]+reasue[j])
    print(str(sps[end])+' '+str(gt[end]))

import sys
n,m,c1,c2= map(int,input().split())
resteam = list(map(int,input().split()))
city = [[sys.maxsize for i in range(0,n)] for i in range(0,n)]
boo = [True for i in range(0,n)]
for i in range(0,m):
    tem = list(map(int,input().split()))
    city[tem[0]][tem[1]],city[tem[1]][tem[0]] = min(sys.maxsize,tem[2]),min(sys.maxsize,tem[2])
dijkstra(city,resteam,n,c1,c2)

