# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:18:07 2018

@author: 1
"""
tem =""
n = input()
n = int(n)
mat = [[0 for i in range(0,n)] for i in range(0,4)]
xm = 0
ym = 0
res = 1

def solve(a):
    maxcount = 0
    for i in range(0,len(a[0])):
        for k in range(i+1,len(a[0])):
            xm = max(a[0][i],a[0][k])
            ym = max(a[1][i],a[1][k])
            count = 0
            for j in range(0,len(a[0])):      
                if a[0][j]<=xm and a[2][j]>xm and a[1][j]<=ym and a[3][j]>ym:
                    count = count +1
            maxcount = max(count,maxcount)
    return maxcount

def output(a):
    print(a)

if n>=2 and n<=50:
    for i in range(0,4):
        tem = input().split()
        for j in range(len(tem)):
            mat[i][j] = int(tem[j])
    count = solve(mat) 
    output(max(count,res))
else:
    print("输入有误，n必须在2到50之间")
    

    