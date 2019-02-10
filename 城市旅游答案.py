# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:48:19 2018

@author: LX
"""

N, K, C1 =input().split()
N, K =int(N), int(K)
haps ={C1:0}
for i in range(N-1):
    city, hap =input().split()
    hap =int(hap)
    haps[city] =hap
G ={}
for i in range(K):
    a, b, c =input().split()
    c =int(c)
    if a in G:
        G[a].update({b:c})
    else:
        G[a] ={b:c}
    if b in G:
        G[b].update({a: c})
    else:
        G[b] ={a: c}
from heapq import heappush, heappop
def dijkstra(G, s, e='ROM'):
    P, D, Q, S =[{}], {s:0}, [(0, s)], set()
    newpair =[]
    while Q:
        _, u =heappop(Q)
        if u in S: 
            continue
        S.add(u)
 
        for v in G[u]:
            inf =float('inf')
            d =D.get(u, inf) +G[u][v]
            if d < D.get(v, inf):
                P[0][v] =u
                D[v] =d
            elif d ==D.get(v, inf):
                newpair.append((v,u))
 
            heappush(Q, (D[v], v))
 
    count =0
    for pair in newpair:
        count +=1
        P.append({})
        for k, u in P[0].items():
            if k ==pair[0]:
                P[count][k] =pair[1]
            else:
                P[count][k] =u
 
        for pair2 in newpair:
            if pair ==pair2: 
                continue
            tmp =count
            count +=1
            P.append({})
            for k, u in P[tmp].items():
                if k ==pair2[0]:
                    P[count][k] =pair2[1]
                else:
                    P[count][k] =u
 
    paths =[]
    for index, p in enumerate(P):
        path =[e]
        for _ in p:
            for k, u in p.items():
                if k ==path[-1]:
                    path.append(u)
        path =path[::-1]
        for i in paths:
            if i ==path:
                break
        else:
            paths.append(path)
 
    maxhap, maxAvghap, dec =0, 0, 0
    for index, path in enumerate(paths):
        th =0
        count =-1
        for city in path:
            count +=1
            th +=haps[city]
        avg =th /count
        if th > maxhap:
            maxhap =th
            if avg > maxAvghap:
                maxAvghap =avg
                dec =index
 
    print(len(paths), D[e], maxhap, int(maxAvghap))
    print('->'.join(map(str, paths[dec])))
 
dijkstra(G, C1)