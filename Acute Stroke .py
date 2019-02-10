# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:07:07 2018

@author: LX

Acute Stroke 

"""


#m,n,l,t = map(int,input().split())
#con = 0
#for i in range(l):
#    lst = []
#    pan = [[False for i in range(n)] for j in range(m)]
#    for j in range(m):
#        lst.append(list(map(int,input().split())))
#    for j in range(1,n-1):
#        for k in range(1,m-1):
#            for l1 in range(j-1,j+2):
#                for l2 in range(k-1,k+2):
#                    if lst[l2][l1]==1 and lst[k][j]==1:
#                        pan[k][j],pan[l2][l1]=True,True
#    for j in range(0,n-1):
#        if lst[0][j]==1 and lst[0][j+1]==1:
#            pan[0][j],pan[0][j+1]=True,True
#        if lst[m-1][j]==1 and lst[m-1][j+1]==1:
#            pan[m-1][j],pan[m-1][j+1]=True,True
#    for j in range(0,m-1):
#        if lst[j][0]==1 and lst[j+1][0]==1:
#            pan[j][0],pan[j+1][0]=True,True
#        if lst[j][n-1]==1 and lst[j+1][n-1]==1:
#            pan[j][n-1],pan[j+1][n-1]=True,True
#    
#    tecon = 0
#    for j in pan:
#        tecon+=j.count(True)
#    con+=tecon
#print(con)

dx,dy,dz = [1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
vol,res = [],0
def bfs(z,y,x):
    global res
    ret = 0
    temp = []
    temp.append([z,y,x])
    ret+=1
    vol[z][y][x]=0
    while temp:
        z,y,x = map(int,temp.pop())
        for i in range(6):
            nz = z+dz[i]
            ny = y+dy[i]
            nx = x+dx[i]
            if (nx<n and nx>=0 and ny<m and ny>=0 and nz<l and nz>=0) and vol[nz][ny][nx]==1:
                vol[nz][ny][nx] = 0
                ret+=1
                temp.append([nz,ny,nx])
    if ret>=t:
        res+=ret
m,n,l,t = map(int,input().split())
for k in range(l):
    lst = []
    for j in range(m):
        lst.append(list(map(int,input().split())))
    vol.append(lst)
for k in range(l):
    for j in range(m):
        for i in range(n):
            if vol[k][j][i]==1:
                bfs(k,j,i)
print(res)



