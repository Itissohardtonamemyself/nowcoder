# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 10:43:57 2018

@author: wentong

function:Public Bike Management

"""
#def panduan(a,b):
#    lst = []
#    lujinlst = [b]
#    for k in range(0,len(a)):
#        if a[k][1]==b:      
#            timelulst = [a[k][2]]
#            cmap = []
#            cmap = a
#            for i in range(0,len(a)):
#                if a[i][1]==b:
#                    lst.append(a[i])
#                    lujinlst.append(a[i][0])
#                    timelulst.append(a[i][2])
#            lujin.append(lujinlst)
#            timelst.append(timelulst)
#            panduanlst.append(lst)
#            for i in lst:
#                cmap.remove(i)
#            for j in range(0,len(lst)):
#                if lst[j][0]!=0:
#                    panduan(cmap,lst[j][0])

#####################回溯法做出来了 好高兴###############################
def panduan(a,b): 
    if b>0:
        lst = []
        lsti = []
        con = 0
        count = 0
        cmap = []
        cmap = a     
        for i in range(0,len(a)):
            if a[i][1]==b:
                shanglujin.append(a[i][1])
                cilujin.append(a[i][0])
                shijian.append(a[i][2])
                con+=1
                lst.append(a[i])
                lsti.append(i)
            if a[i][0]==b:
                shanglujin.append(a[i][0])
                cilujin.append(a[i][1])
                shijian.append(a[i][2])
                con+=1
                lst.append(a[i])
                lsti.append(i)
        panduanlst.append(lst)
        if len(lujin)!=0:
            for k in range(0,len(lujin)):
                    for l in range(0,con):
                        if len(lujin[k])>0:
                            if lujin[k][len(lujin[k])-1]==shanglujin[l]:
                                count +=1
                    for i in range(0,count):
                        lujin.append(lujin[k])
                        lujintime.append(lujintime[k])
            for k in range(0,len(lujin)):
                    for l in range(0,con):
                        if len(lujin[k])>0:
                            if lujin[k][len(lujin[k])-1]==shanglujin[l]:                
                                lujin[k].append(cilujin[l])
                                lujintime[k].append(shijian[l])
                                del shanglujin[l]
                                del cilujin[l]
                                del shijian[l]    
        for i in lst:
            cmap.remove(i)
        else:
            for i in range(0,con):
                    lujin.append([b])
                    lujintime.append([])
        for j in range(0,len(lst)):
            panduan(cmap,lst[j][0])
def shucheche(b):
    cheche = 0
    if b>cmax//2:
        cheche = cmax//2
    elif b<=cmax//2:
        cheche = cmax//2+1 - b
    return cheche
def shuche(a):
  che = 0
  if a<cmax:
        che = cmax//2
  elif a>=cmax:
        che = a-cmax+1
  return che
#优先级为先最短路径，而后最少车辆
cmax,n,sp,m = map(int,input().strip().split())#问题站只有一个。。。
si = [i for i in range(1,n+1)]
cilst = list(map(int,input().strip().split()))
maptime = []
panduanlst = []
lujin = []
lujintime=[]
cilujin = []
shanglujin = []
shijian = []
for i in range(0,m):
    maptime.append(list(map(int,input().strip().split())))
maptime.sort(key=lambda x :(x[0],x[1],x[2]))
#反正只有一个，不需要多想了
panduan(maptime,sp)
timelu = []
timefan = []
cheres = []
lastin = 0
lastout = 0
he = 0
for k in lujintime:
    timelu.append(sum(k))
if len(timelu)>0:
    dtime = min(timelu)
    for k in range(0,len(timelu)):
        if dtime==timelu[k]:
            if  cilst[lujin[k][0]-1]>=cmax//2 :
                if len(lujin[k])>=3:
                    for j in range(1,len(lujin[k])-1):
                        he = cilst[lujin[k][j]-1]+he+cmax
                    if he<=cmax//2*(len(lujin[k])-1):
                        lastin = 0
                    else:
                        lastin = he - cmax//2*(len(lujin[k])-1)
                    cheres.append([timelu[k],k,lastin,0])#j判断到没到最后的站。tem要运多少车回去
                else:
                    cheres.append([timelu[k],k,cilst[sp-1]-cmax//2,0])
            elif cilst[lujin[k][0]-1]<=cmax//2:
                if len(lujin[k])>=3:
                    he = 0
                    for j in range(1,len(lujin[k])-1):
                        he = cilst[lujin[k][j]-1]+he
                        if he>=cmax//2*(len(lujin[k])-1):
                            lastout = 0
                        else:
                            lastout = cmax//2*(len(lujin[k])-1) - he 
                    cheres.append([timelu[k],k,0,lastout])#，j判断到没到最后的站。tem要运多少车回去
                else:
                    cheres.append([timelu[k],k,0,cmax//2-cilst[sp-1]])
    cheres.sort(key = lambda x:(x[3]))
    outstr = ''
    if cheres[0][2]==0:
        if (len(lujin[cheres[0][1]])-1)>=2:
            for i in range(0,len(lujin[cheres[0][1]])-1):
               outstr = outstr+str(lujin[cheres[0][1]][len(lujin[cheres[0][1]])-i-1])+"->"
            outstr = outstr + str(lujin[cheres[0][1]][0])
            print(cheres[0][3],outstr,cheres[0][2])
        else:
            print(cheres[0][3],str(0)+"->"+str(lujin[cheres[0][1]][0]),cheres[0][2])
    elif cheres[0][3]==0:     
         if (len(lujin[cheres[0][1]])-1)>=2:
            for i in range(0,len(lujin[cheres[0][1]])-1):
               outstr = outstr+str(lujin[cheres[0][1]][i])+"->"
            outstr = outstr + str(lujin[cheres[0][1]][len(lujin[cheres[0][1]])-1])
            print(cheres[0][3],outstr,cheres[0][2])
         else:
             print(cheres[0][3],str(0)+"->"+str(lujin[cheres[0][1]][0]),cheres[0][2])
else:
    pass

#链接：https://www.nowcoder.com/questionTerminal/4b20ed271e864f06ab77a984e71c090f
#来源：牛客网
#
#def dfs(sta): global e,n_sta,problem_sta,way,temp,min,book
#    way.append(sta) if sta == problem_sta:
#        c = []
#        t = 0  for n in range(len(way)-1):
#            t += e[way[n]][way[n+1]] if min == 0:
#            min = t for i in way:
#                c.append(i)
#            temp = []
#            temp.append(c) elif min > t:
#            min = t
#            temp = [] for i in way:
#                c.append(i)
#            temp.append(c) elif min == t: for i in way:
#                c.append(i)
#            temp.append(c) else: for i in range(n_sta+1): if sta == problem_sta: break  elif (e[sta][i] != 0) and (book[i] == 0):
#                book[i] = 1  dfs(i)
#                book[i] = 0  way.pop(-1)
#Cmax,n_sta,problem_sta,n_road = [int(x) for x in input().split()]
#n_bike = [int(x) for x in input().split()]
#road,way = [],[]
#min = 0 need = 0 e = [[0 for i in range(n_sta+1)] for n in range(n_sta+1)]
#book = [0 for i in range(n_sta)]
#book.insert(0,1) for i in range(n_road):
#    road.append([int(x) for x in input().split()]) for r in road:
#    e[r[0]][r[1]] = r[2]
#    e[r[1]][r[0]] = r[2]
#dfs(0)
#best = temp[0]
#no = 0 max_bike = 10**9 for x,t in enumerate(temp):
#    max_bike0 = 0  need = [] for i in t[1:]:
#        need.append( Cmax/2 - n_bike[i-1] ) if sum(need)>max_bike0:
#            max_bike0 = sum(need) if max_bike>max_bike0:
#        max_bike = max_bike0
#        no = x
#needWay = temp[no]
#n_have = 0 for i in needWay[1:]:
#    n_have += (n_bike[i-1])
#need = max_bike
#more =need + n_have - Cmax*(len(needWay)-1)/2  print(int(need),'->'.join([str(x) for x in best]),int(more))
    

#链接：https://www.nowcoder.com/questionTerminal/4b20ed271e864f06ab77a984e71c090f
#来源：牛客网
#这个测试用例说明。。。这他妈的更本就没有单向路径。。。。尼玛的都可以反着推的！！！
#测试用例:
#temmap = []
#temmap = maptime
#100 10 3 45
#7 2 46 42 42 26 2 25 44 41
#0 1 4
#0 2 10
#0 3 6
#0 4 3
#0 5 1
#0 6 6
#0 7 10
#0 8 8
#0 9 2
#1 2 7
#1 3 4
#1 4 10
#1 5 8
#1 6 8
#1 7 6
#1 8 4
#1 9 3
#2 3 1
#2 3 1
#2 5 1
#2 6 10
#2 7 10
#2 8 6
#2 9 5
#3 4 6
#3 5 10
#3 6 2
#3 7 3
#3 8 7
#3 9 10
#4 5 6
#4 6 9
#4 7 1
#4 8 4
#4 9 9
#5 6 9
#5 7 2
#5 8 8
#5 9 3
#6 7 9
#6 8 6
#6 9 1
#7 8 5
#7 9 4
#8 9 4
#
#对应输出应该为:
#
#60 0->5->2->3 0
#
#你的输出为:
#
#4 0->3 0
maptime.append([0,1,4])
maptime.append([0,2,10])
maptime.append([0,3,6])
maptime.append([0,4,3])
maptime.append([0,5,1])
maptime.append([0,6,6])
maptime.append([0,7,10])
maptime.append([0,8,8])
maptime.append([0,9,2])
maptime.append([1,2,7])
maptime.append([1,3,4])
maptime.append([1,4,10])
maptime.append([1,5,8])
maptime.append([1,6,8])
maptime.append([1,7,6])
maptime.append([1,8,4])
maptime.append([1,9,3])
maptime.append([2,3,1])
maptime.append([2,3,1])
maptime.append([2,5,1])
maptime.append([2,6,10])
maptime.append([2,7,10])
maptime.append([2,8,6])
maptime.append([2,9,5])
maptime.append([3,4,6])
maptime.append([3,5,10])
maptime.append([3,6,2])
maptime.append([3,7,3])
maptime.append([3,8,7])
maptime.append([3,9,10])
maptime.append([4,5,6])
maptime.append([4,6,9])
maptime.append([4,7,1])
maptime.append([4,8,4])
maptime.append([4,9,9])
maptime.append([5,6,9])
maptime.append([5,7,2])
maptime.append([5,8,8])
maptime.append([5,9,3])
maptime.append([6,7,9])
maptime.append([6,8,6])
maptime.append([6,9,1])
maptime.append([7,8,5])
maptime.append([7,9,4])
maptime.append([8,9,4])