# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:43:13 2018

@author: LX

PAT Judge

"""

n,k,m = map(int,input().split())
kmark = list(map(int,input().split()))
lst = []
user = [[None for j in range(k)] for i in range(10001)]
for i in range(m):
    tem = list(map(int,input().split()))
    if tem[2]!=-1 and (user[tem[0]][tem[1]-1]==None or user[tem[0]][tem[1]-1]<=tem[2]):
        user[tem[0]][tem[1]-1] = tem[2]
    elif tem[2]==-1 and user[tem[0]][tem[1]-1]==None:#注意原来输入了-1 后来输入了0 要由0.0更新为0
        user[tem[0]][tem[1]-1] = 0.0
selected = []
for i in range(0,len(user)):
    for j in user[i]:
        if isinstance(j, int):     
            selected.append([i,0]+user[i])
            break
for i in range(0,len(selected)):
    tcon = 0
    for j in range(2,len(selected[i])):
        if selected[i][j]==kmark[j-2]:
            tcon+=1
    selected[i] = selected[i]+[tcon]
for i in selected:
    for j in range(2,len(i)-1):
        if i[j]!=None:
            i[1]+=i[j]
        else:
            i[j] = '-'
selected.sort(key = lambda x:(-x[1],-x[k+2],x[0]))
selected[0][0] = '%05d'%selected[0][0]
selected[0].pop()
for j in range(1,len(selected[0])):
    if isinstance(selected[0][j],float):
        selected[0][j] = int(selected[0][j])
print(1,' '.join(map(str,selected[0])))
con1,con2,st = 1,1,selected[0][1]
for i in range(1,len(selected)):
    if selected[i][1]!=st:
        con1+=con2
        con2=1
        st = selected[i][1]
    else:
        con2+=1
    selected[i][0] = '%05d'%selected[i][0]
    selected[i].pop()
    for j in range(1,len(selected[i])):
        if isinstance(selected[i][j],float):
            selected[i][j] = int(selected[i][j])
    print(con1,' '.join(map(str,selected[i])))
