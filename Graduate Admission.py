# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:36:00 2018

@author: LX

Graduate Admission

"""

ranklst = []
n,m,k = map(int,input().split())
#boolst = [True for i in range(n)]
out = [[] for i in range(m)]
dinge = list(map(int,input().split()))
lst = []
for i in range(n):
    te = list(map(int,input().split()))
    te.append(i)
    lst.append(te)
lst.sort(key=lambda x:(-x[0]-x[1],-x[0]))
ran,ran1 = 0,1
for i in range(0,len(lst)-1):
    lst[i].append(ran)
    for j in range(i+1,len(lst)):
        if lst[i][0]==lst[j][0] and (lst[i][0]+lst[i][1])==(lst[j][0]+lst[j][1]):
            ran1+=1
            break
        else:
            ran+=ran1
            ranklst.append(i+1)
            ran1=1
            break
lst[len(lst)-1].append(ran)
ranklst.append(n)
ranklst = [0]+ranklst
backup = list(lst)
#如果是学校挑人的话：
#for i in range(2,2+k):
#     #同一排名的输入
# for j in range(0,len(ranklst)-1):
#     for l in range(ranklst[j],ranklst[j+1]):
#         if boolst[l]:
#             te = set([])
#             if dinge[lst[l][i]]>0 or (lst[l][i] in te):
#                 te.add(lst[l][i])
#                 out[lst[l][i]].append(str(lst[l][-2]))
#                 boolst[l]=False
#                 dinge[lst[l][i]]-=1
con=0
for i in range(0,len(ranklst)-1):
    te = set([])
    for j in range(ranklst[i],ranklst[i+1]):
        for l in range(2,2+k):
            if dinge[lst[j][l]]>0 or (lst[j][l] in te):
                te.add(lst[j][l])
                out[lst[j][l]].append(lst[j][-2])
                dinge[lst[j][l]]-=1
                lst[j].append(False)
                con+=1
                break
while con:
    for i in lst:
        if not i[-1]:
            lst.remove(i)
            con-=1
if lst:
    ranka= []
    lst.sort(key=lambda x:(-x[0]-x[1],-x[0]))
    ran,ran1 = 0,1
    for i in range(0,len(lst)-1):
        lst[i].append(ran)
        for j in range(i+1,len(lst)):
            if lst[i][0]==lst[j][0] and (lst[i][0]+lst[i][1])==(lst[j][0]+lst[j][1]):
                ran1+=1
                break
            else:
                ran+=ran1
                ranka.append(i+1)
                ran1=1
                break
    lst[len(lst)-1].append(ran)
    ranka.append(len(lst))
    ranka = [0]+ranka
    for i in range(0,len(ranka)-1):
        te = set([])
        for j in range(ranka[i],ranka[i+1]):
            for l in range(2,2+k):
                if dinge[lst[j][l]]>0 or (lst[j][l] in te):
                    te.add(lst[j][l])
                    out[lst[j][l]].append(lst[j][-2])
                    dinge[lst[j][l]]-=1
    #                lst[j].append(False)
                    break              
for i in out:
   if i:
      i.sort()
      print(' '.join(map(str,i)))  
   else:
      print()         



