# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:37:13 2018

@author: wentong

function：城市旅游提升算法效率的更新版本

"""
import sys
fs = input().split()
n = int(fs[0])
k = int(fs[1])
city = fs[2]
haplst = []
temlst = []
for i in range(0,n-1):
    temlst = input().split()
    haplst.append([temlst[0],int(temlst[1])])
costlst = []
boo = []
for i in range(0,k):
    temlst = input().split()
    boo.append(1)
    boo.append(1)
    costlst.append([temlst[0],temlst[1],int(temlst[2])])
    costlst.append([temlst[1],temlst[0],int(temlst[2])])
#找起点
startindex = []
startcity,endcity = city,''
for i in range(0,len(costlst)):
    if costlst[i][0] == city:
        startindex.append(i)
    
micost,mahpa,maavg,avghap = sys.maxsize,-1,-1,0
adj,temroad,cost,con,conhap,k,brecon = [],[],0,0,0,0,0
conroad = 0
k = startindex[0]
temroad.append(city)
while len(startindex)>0:
    if boo[k]==1 and startcity==costlst[k][0]:
        endcity = str(costlst[k][1])
        con = int(con +costlst[k][2])
        for l in haplst:
            if l[0]==endcity:
                conhap = conhap + l[1]
        temroad.append(endcity)
        startcity = str(endcity)
        if k%2 ==0:
            boo[k],boo[k+1]=0,0
        else:
            boo[k],boo[k-1]=0,0   
        if endcity == 'ROM':
            avghap = int(conhap//(len(temroad)-1))
            if con<micost:
                adj = list(temroad)
                cost = int(con)
                mahpa = int(conhap)
                maavg = int(avghap)
                micost = int(con)
                conroad = 0
            elif con == micost and conhap>mahpa:
                adj = list(temroad)
                cost = int(con)
                mahpa = int(conhap)
                maavg = int(avghap)
                micost = int(con)
            elif con == micost and conhap==mahpa and avghap>maavg:
                adj = list(temroad)
                cost = int(con)
                mahpa = int(conhap)
                maavg = int(avghap)
                micost = int(con)
            if con==micost:
                conroad+=1
            temroad = []
            con = 0
            conhap = 0
            brecon = 0
            del startindex[0]
            if len(startindex)==0:
                break
            k = int(startindex[0])
            startcity=str(costlst[k][0])
            temroad.append(startcity)
            boo = [1 for i in range(0,len(boo))]
        else:
            k+=1    
            if k==len(costlst):
                k=0     
    #如果说有一条线路怎么走都走不通，那么，这个时候就要跳出当前搜索
            brecon+=1
            if brecon>=2*len(costlst):
                temroad = []
                con = 0 
                conhap = 0
                del startindex[0]
                if len(startindex)==0:
                    break
                k = int(startindex[0])
                startcity=str(costlst[k][0])
                temroad.append(startcity)
                boo = [1 for i in range(0,len(boo))]
                brecon=0
    else:
        k+=1
        if k==len(costlst):
            k = 0 
        brecon+=1
        if brecon>=2*len(costlst):
                temroad = []
                con = 0 
                conhap = 0
                del startindex[0]
                if len(startindex)==0:
                    break
                k = int(startindex[0])
                startcity=str(costlst[k][0])
                temroad.append(startcity)
                boo = [1 for i in range(0,len(boo))]
                brecon=0
print(str(conroad)+" "+str(cost)+" "+str(mahpa)+" "+str(maavg))
for i in range(0,len(adj)-1):
    print(adj[i]+"->",end='')
print(adj[len(adj)-1])