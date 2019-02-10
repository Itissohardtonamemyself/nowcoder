# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:25:10 2018

@author: 1
"""

#p,g = map(int,input().split())
#lst = list(map(int,input().split()))
#temlst = []
#num = list(map(int,input().split()))
#for i in range(0,len(num)):
#    temlst.append(lst[num[i]])
#lst = list(temlst)
#temlst = []
#num1 = [0 for i in range(len(num))]
#for i in range(0,len(num)):
#    num1[num[i]] = i
##for i in range(0,p-1):
##    for j in range(0,p-i-1):
##        if num[j]>num[j+1]:
##            num[j],num[j+1] = num[j+1],num[j]
##            lst[j],lst[j+1] = lst[j+1],lst[j]
#ranlst = [0 for i in range(0,p)]
#
#temlst,nextlst,count,con = [],[],0,0
#
#def loop(a):
#    for i in range(0,len(ranlst)):
#        if ranlst[i]==0:
#            if a==1:
#                a-=1
#            else:
#                ranlst[i]=-1
#                return
#while len(lst)>=g:
#    for i in range(len(lst)//g):
#        for j in range(g):
#            temlst.append(lst[i*g+j])
#        nextlst.append(max(temlst))
#        for k in range(g):
#            if count ==0:
#                if temlst[k]!=max(temlst):
#                    ranlst[i*g+k] = -1
#            else:
#                if temlst[k]==max(temlst):
#                    con = 1
#                else:
#                    loop(con)
#        temlst = []
#    for i in range(len(lst)//g*g,len(lst)):
#        temlst.append(lst[i])
#    if len(temlst)>0:
#        nextlst.append(max(temlst))
#    for k in range(len(lst)//g*g,len(lst)):
#        if count ==0:
#            if temlst[k-len(lst)//g*g]!=max(temlst):
#                ranlst[k] = -1
#        else:
#            if temlst[k-len(lst)//g*g]==max(temlst):
#                con = 1
#            else:
#                loop(con)
#    temlst = []
#    leng = len(nextlst) 
#    for i in range(len(ranlst)):
#        if ranlst[i]==-1:
#            ranlst[i]=1+leng
#    lst = list(nextlst)
#    nextlst = []
#    count = 1
#temlst = []
#if len(lst)==2:
#    if lst[0]>lst[1]:
#        for i in range(len(ranlst)):
#            if ranlst[i]==0:
#                temlst.append(i)
#        ranlst[temlst[0]],ranlst[temlst[1]]=1,2
#    if lst[0]<lst[1]:
#        for i in range(len(ranlst)):
#            if ranlst[i]==0:
#                temlst.append(i)
#        ranlst[temlst[0]],ranlst[temlst[1]]=2,1
#    if lst[0]==lst[1]:
#        for i in range(len(ranlst)):
#            if ranlst[i]==0:
#                ranlst[i]=1
#if len(lst)==1:
#    for i in range(0,len(ranlst)):
#        if ranlst[i]==0:
#            ranlst[i]=1
#            break
#for i in range(len(num1)-1):
#    print(str(ranlst[num1[i]])+" ",end='')
#print(ranlst[num1[len(num1)-1]])        

np,ng = map(int,input().split())
w = list(map(int, input().split()))
od = list(map(int, input().split()))
ans = [1 for i in range(np)]
t = len(set(w))
while t > 1:    # 直到剩的值，只有1个
        newod = []
        for i in range(0, len(od), ng):
                p = od[i:i+ng]
                mx = max((w[x] for x in p))
                for x in p:
                        if w[x] == mx:
                                newod.append(x)
        for x in od:
            if x not in newod:
                ans[x] = len(newod)+1
        t = len(set(w[x] for x in newod))
        od = [x for x in newod]
print(' '.join(map(str,ans)))
