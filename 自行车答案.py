# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:10:37 2018

@author: 错的
"""
def dfs(sta):
    global e,n,sp,way,temp,mini,book
    if sta == sp:
        way.append(sta)
    c = []
    t = 0
    for n in range(len(way)-1):
        t+=e[way[n]][way[n+1]]
        if mini == 0:
            mini = t
            for i in way:
                c.append(i)
            temp = []
            temp.append(c)
        elif mini>t:
                mini = t
                temp = []
                for i in way:
                    c.append(i)
                temp.append(c)
        elif mini == t:
            for i in way:
                c.append(i)
                temp.append(c)
        else:
            for i in range(n+1):
                if sta == sp:
                    book[i] = 1
                    dfs(i)
                    book[i] = 0
                    way.pop(-1)

cmax,n,sp,m = [int(x) for x in input().split()]
n_bike = [int(x) for x in input().split()]
road,way = [],[]
mini = 0  
need = 0 
e =[[0 for i in range(n+1)] for n in range(n+1)]
book = [0 for i in range(n)]
book.insert(0,1) 
for i in range(m): 
    road.append([int(x) for x in input().split()]) 
    for r in road:    
        e[r[0]][r[1]] = r[2]
        e[r[1]][r[0]] = r[2]
dfs(0)
best = temp[0]
no = 0 
max_bike = 10**9 
for x,t in enumerate(temp):
    max_bike0 = 0
    need = []
    for i in t[1:]:
        need.append(cmax/2-n_bike[i-1])
        if sum(need)>max_bike0:
            max_bike0 = sum(need)
        if max_bike>max_bike0:
            max_bike = max_bike0
            no = x
n_have=0
needWay = temp[no]
for i in needWay[1:]:
    n_have+=(n_bike[i-1])
need = max_bike
more = need+n_have-cmax*(len(needWay)-1)/2
print(int(need),"->".join([str(x) for x in best]),int(more))

#
#def panduan(a,b): 
#    if b>0:
#        lst = []
#        con = 0
#        cmap = []
#        cmap = a     
#        for i in range(0,len(a)):
#            if a[i][1]==b:
#                shanglujin.append(a[i][1])
#                cilujin.append(a[i][0])
#                shijian.append(a[i][2])
#                con+=1
#                lst.append(a[i])
#            if a[i][0]==b:
#                shanglujin.append(a[i][0])
#                cilujin.append(a[i][1])
#                shijian.append(a[i][2])
#                con+=1
#                lst.append(a[i])
#        panduanlst.append(lst)
#        if len(lujin)!=0:
#            for k in range(0,len(lujin)):
#                    for i in range(0,con):
#                        if len(lujin[k])>0 and len(shanglujin)==con:
#                            if lujin[k][len(lujin[k])-1]==shanglujin[i]:
#                                lujin[k].append(cilujin[i])
#                                lujintime[k].append(shijian[i])
#                                del shanglujin[i]
#                                del cilujin[i]
#                                del shijian[i]
#                            
#        else:
#            for i in range(0,con):
#                    lujin.append([b])
#                    lujintime.append([])
#        for i in lst:
#            cmap.remove(i)
#        for j in range(0,len(lst)):
#            panduan(cmap,lst[j][0])
#def shucheche(b):
#    cheche = 0
#    if b>cmax//2:
#        cheche = cmax//2
#    elif b<=cmax//2:
#        cheche = cmax//2+1 - b
#    return cheche
#
#def shuche(a):
#  che = 0
#  if a<cmax:
#        che = cmax//2
#  elif a>=cmax:
#        che = a-cmax+1
#  return che
##优先级为先最短路径，而后最少车辆
#cmax,n,sp,m = map(int,input().strip().split())#问题站只有一个。。。
#si = [i for i in range(1,n+1)]
#cilst = list(map(int,input().strip().split()))
#maptime = []
#panduanlst = []
#lujin = []
#lujintime=[]
#cilujin = []
#shanglujin = []
#shijian = []
#for i in range(0,m):
#    maptime.append(list(map(int,input().strip().split())))
#maptime.sort(key=lambda x :(x[0],x[2]))
##反正只有一个，不需要多想了
#panduan(maptime,sp)
#timelu = []
#timefan = []
#cheres = []
#lastin = 0
#lastout = 0
#he = 0
#for k in lujintime:
#    timelu.append(sum(k))
#if len(timelu)>0:
#    dtime = min(timelu)
#    for k in range(0,len(timelu)):
#        if dtime==timelu[k]:
#            if  cilst[lujin[k][0]-1]>=cmax//2 :
#                if len(lujin[k])>=3:
#                    for j in range(1,len(lujin[k])-1):
#                        he = cilst[lujin[k][j]-1]+he+cmax
#                    if he<=cmax//2*(len(lujin[k])-1):
#                        lastin = 0
#                    else:
#                        lastin = he - cmax//2*(len(lujin[k])-1)
#                    cheres.append([timelu[k],k,lastin,0])#j判断到没到最后的站。tem要运多少车回去
#                else:
#                    cheres.append([timelu[k],k,cilst[sp-1]-cmax//2,0])
#            elif cilst[lujin[k][0]-1]<=cmax//2:
#                if len(lujin[k])>=3:
#                    he = 0
#                    for j in range(1,len(lujin[k])-1):
#                        he = cilst[lujin[k][j]-1]+he
#                        if he>=cmax//2*(len(lujin[k])-1):
#                            lastout = 0
#                        else:
#                            lastout = cmax//2*(len(lujin[k])-1) - he 
#                    cheres.append([timelu[k],k,0,lastout])#，j判断到没到最后的站。tem要运多少车回去
#                else:
#                    cheres.append([timelu[k],k,0,cmax//2-cilst[sp-1]])
#    cheres.sort(key = lambda x:(x[3]))
#    outstr = ''
#    if cheres[0][2]==0:
#        if (len(lujin[cheres[0][1]])-1)>=2:
#            for i in range(0,len(lujin[cheres[0][1]])-1):
#               outstr = outstr+str(lujin[cheres[0][1]][len(lujin[cheres[0][1]])-i-1])+"->"
#            outstr = outstr + str(lujin[cheres[0][1]][0])
#            print(cheres[0][3],outstr,cheres[0][2])
#        else:
#            print(cheres[0][3],str(0)+"->"+str(lujin[cheres[0][1]][0]),cheres[0][2])
#            
#    elif cheres[0][3]==0:     
#         if (len(lujin[cheres[0][1]])-1)>=2:
#            for i in range(0,len(lujin[cheres[0][1]])-1):
#               outstr = outstr+str(lujin[cheres[0][1]][i])+"->"
#            outstr = outstr + str(lujin[cheres[0][1]][len(lujin[cheres[0][1]])-1])
#            print(cheres[0][3],outstr,cheres[0][2])
#         else:
#             print(cheres[0][3],str(0)+"->"+str(lujin[cheres[0][1]][0]),cheres[0][2])
#else:
#    pass