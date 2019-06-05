# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:56:12 2018

@author: LX

Total Sales of Supply Chain

"""

def dfs(root,bu):
    global res
    boo = True
    for i in range(0,len(lst[root])):
        rt = lst[root][i]
        boo = False
        dfs(rt,bu+1)
    if boo:
        res+=p*pow(1+r*0.01,bu)*sa[root]
res = 0.0
n,p,r = map(float,input().split())
lst,sa,con = [],[],0
for i in range(0,int(n)):
    temp = list(map(int,input().split()))
    if temp[0]!=0:
        con+=1
        lst.append(temp[1:])
        sa.append([])
    else:
        sa.append(temp[1])
        lst.append([])
dfs(0,0)
print("%.1f"%res)
