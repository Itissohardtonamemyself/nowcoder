# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:01:06 2018

@author: LX

The Best Rank 

"""

g1,g2,g3,g4 = [],[],[],[]
stu = {}
n,m = map(int,input().split())
for i in range(n):
    t = input().split()
#    stu[t[0]]=[(int(t[1])+int(t[2])+int(t[3]))//3,int(t[1]),int(t[2]),int(t[3])]
    g1.append([t[0],(int(t[1])+int(t[2])+int(t[3]))//3])
    g2.append([t[0],int(t[1])])
    g3.append([t[0],int(t[2])])
    g4.append([t[0],int(t[3])])
g1.sort(key = lambda x:(-x[1]))
g2.sort(key = lambda x:(-x[1]))
g3.sort(key = lambda x:(-x[1]))
g4.sort(key = lambda x:(-x[1]))

con = 1
stu[g1[0][0]],temp = [con,'A'],g1[0][1]
for i in range(1,n):
    if g1[i][1]==temp:
        stu[g1[i][0]] = [con,'A']
    else:
        con = i+1
        temp = g1[i][1]
        stu[g1[i][0]] = [con,'A']

con = 1
temp = g2[0][1]
if stu[g2[0][0]][0]>con:
   stu[g2[0][0]] = [con,'C'] 
for i in range(1,n):
    if g2[i][1]==temp:
        if stu[g2[i][0]][0]>con:
            stu[g2[i][0]] = [con,'C']
    else:
        con = i+1
        temp = g2[i][1]
        if stu[g2[i][0]][0]>con:
            stu[g2[i][0]] = [con,'C']

con = 1
temp = g3[0][1]
if stu[g3[0][0]][0]>con:
   stu[g3[0][0]] = [con,'M'] 
for i in range(1,n):
    if g3[i][1]==temp:
        if stu[g3[i][0]][0]>con:
            stu[g3[i][0]] = [con,'M']
    else:
        con = i+1
        temp = g3[i][1]
        if stu[g3[i][0]][0]>con:
            stu[g3[i][0]] = [con,'M']
con = 1
temp = g4[0][1]
if stu[g4[0][0]][0]>con:
   stu[g4[0][0]] = [con,'E'] 
for i in range(1,n):
    if g4[i][1]==temp:
        if stu[g4[i][0]][0]>con:
            stu[g4[i][0]] = [con,'E']
    else:
        con = i+1
        temp = g4[i][1]
        if stu[g4[i][0]][0]>con:
            stu[g4[i][0]] = [con,'E']
for j in range(m):
    query = input()
    if query not in stu:
        print("N/A")
    else:
        print(str(stu[query][0])+" "+stu[query][1])
#for j in range(m):
#    query = input()
#    if query not in stu:
#        print("N/A")
#    else:
#        mi = -1
#        for k in range(n):
#            if stu[query][0]==g1[k] and k>mi:
#                best = 'A'
#                rank = n-k
#                mi = k
#            if stu[query][1]==g2[k] and k>mi:
#                best = 'C'
#                rank = n-k
#                mi = k
#            if stu[query][2]==g3[k] and k>mi:
#                best = 'M'
#                rank = n-k
#                mi = k
#            if stu[query][3]==g4[k] and k>mi:
#                best = 'E'
#                rank = n-k
#                mi = k
#        print(str(rank)+" "+best)

