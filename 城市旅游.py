# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:18:07 2018

@author: wentong

function:最小路径 获得最大快乐收益
每个输入文件包含一个测试样本
每个测试样本，第一行包含包含2个正整数(2<=N<=200)为城市数N和总路数K 跟着是开始城市的名字
以下N-1行包含有城市名 和快乐收益 除了开始的城市
然后k行 描述 城市1-2和花费cost
ROM是旅游终点


输出：
优先级： 最少花费，最大快乐收益，最大平均收益（收益/城市数）
最小花费对应的不同路线数，花费，快乐收益，平均快乐收益（取整数部分）
路线-》。。。

"""

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
        
adj,temroad,cost,con,k,brecon = [],[],[],0,0,0
k = startindex[0]
temroad.append(city)
while len(startindex)>0:
    if boo[k]==1 and startcity==costlst[k][0]:
        endcity = str(costlst[k][1])
        con = int(con +costlst[k][2])
        temroad.append(endcity)
        startcity = str(endcity)
        if k%2 ==0:
            boo[k],boo[k+1]=0,0
        else:
            boo[k],boo[k-1]=0,0   
        if endcity == 'ROM':
            adj.append(temroad)
            cost.append(con)
            temroad = []
            con = 0
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
                del startindex[0]
                if len(startindex)==0:
                    break
                k = int(startindex[0])
                startcity=str(costlst[k][0])
                temroad.append(startcity)
                boo = [1 for i in range(0,len(boo))]
                brecon=0
mi = min(cost)
minadj,mincost = [],[]
for i in range(0,len(cost)):
    if cost[i]==mi:
        minadj.append(adj[i])
        mincost.append(cost[i])
nroad = str(len(minadj))
con = 0
conlst = []
for i in minadj:
    for j in i:
        for k in range(0,len(haplst)):
            if j==haplst[k][0]:
                con = con + haplst[k][1]
    conlst.append(con)
    con = 0
ma = max(conlst)
mahap = []
for i in range(0,len(conlst)):
    if conlst[i]==ma:
        mahap.append(conlst[i])
    else:
        del minadj[i]
        del mincost[i]
maavehap = []
con = 0
for i in range(0,len(mahap)):
    con = mahap[i]//(len(minadj[i])-1)
    maavehap.append(con)
    con = 0
ma = max(maavehap) 
avehap = list(maavehap)
for i in range(0,len(maavehap)):
    if maavehap[i]!=ma:
        del avehap[i]
        del mahap[i]
        del minadj[i]
        del mincost[i]
c = str(mincost[0])
gainhap = str(mahap[0])
gainavehap = str(avehap[0])
print(nroad+" "+c+" "+gainhap+" "+gainavehap)
for i in range(0,len(minadj[0])-1):
    print(minadj[0][i]+"->",end='')
print(minadj[0][len(minadj[0])-1])