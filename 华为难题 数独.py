# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:04:15 2019

@author: LX

华为难题 数独

"""

def find(x,y):
    hadnum = set([])
    for i in range(9):
        hadnum.add(mat[x][i])
        hadnum.add(mat[i][y])
    for i in range(3):
        for j in range(3):
            hadnum.add(mat[x//3*3+i][y//3*3+j])
    rest = []
    for i in range(1,10):
        if i not in hadnum:
            rest.append(i)
    
    for i in rest:
        mat[x][y] = i
        nx,ny,fd = -1,-1,0
        for j in range(9):
            for k in range(9):
                if mat[j][k] == 0:
                    nx = j
                    ny = k
                    fd = 1
                    break
            if fd==1:
                break
        if nx==-1:
            return True
        if find(nx,ny):
            mat[x][y]=i
            return True
        else:
            mat[x][y] = 0
    return False

mat = []
for i in range(9):
    mat.append(list(map(int,input().split())))
nx,ny,fd = -1,-1,0
for j in range(9):
    for k in range(9):
        if mat[j][k] == 0:
            nx = j
            ny = k
            fd = 1
            break
    if fd==1:
        break
find(nx,ny)
for i in mat:
    print(' '.join(map(str,i)))