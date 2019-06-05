# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:57:07 2018

@author: Liu WENTONG

"""

lst = list(map(int,input().split()))
num, l, h = lst[0],lst[1],lst[2]
alst,l1,l2,l3,l4,l5 = [],[],[],[],[],[] 
for j in range(num):
    alst.append(list(map(int,input().split()))) 
for i in range(num):  
    if alst[i][1] >= h and alst[i][2] >= h:
        l1.append(alst[i])  
    elif alst[i][1] >= h and alst[i][2] < h and alst[i][2] >= l:
        l2.append(alst[i])  
    elif alst[i][1] < h and alst[i][2] < h and alst[i][1] >= alst[i][2] and alst[i][1] >= l and alst[i][2] >= l:
        l3.append(alst[i])  
    elif alst[i][1] >= l and alst[i][2] >= l and alst[i][1] < h:
        l4.append(alst[i]) 
    else:
        l5.append(alst[i])
l1.sort(key=lambda x:((-x[1]-x[2],-x[1],x[0])))#x是其中的每个list 这排序是对元祖格式的数据有效的
l2.sort(key=lambda x:((-x[1]-x[2],-x[1],x[0])))
l3.sort(key=lambda x:((-x[1]-x[2],-x[1],x[0])))
l4.sort(key=lambda x:((-x[1]-x[2],-x[1],x[0])))
l5.sort(key=lambda x:((-x[1]-x[2],-x[1],x[0])))#排列的顺续默认是升序。有负号 代表降序，优先级排序由左至右。
li = l1+l2+l3+l4+l5 
print(num-len(l5),end='\n') 
for t in range(num-len(l5)):  
    print("%d %d %d"%(li[t][0],li[t][1],li[t][2]),end='\n')