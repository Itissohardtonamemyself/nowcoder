# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:26:15 2018

@author: LX

function:
    给定一个常数K以及一个单链表L，请编写程序将L中每K个结点反转。例如：给定L为1→2→3→4→5→6，K为3，则输出应该为
3→2→1→6→5→4；如果K为4，则输出应该为4→3→2→1→5→6，即最后不到K个元素不反转。

"""

address,N,K  = input().strip().split()
N = int(N)
K = int(K)
ma = []
def tran(a,b,c):
    for k in range(0,b):
        c.append(a[len(a)-k-1])
    return c
def make(ma1,tem3,lst1):
    for i in range(0,len(ma1)):
        if ma1[i][0] == tem3:
            lst1.append(ma1[i])
            tem3 = ma1[i][2]
            ma1.remove(ma1[i])
            break
    return ma1,tem3,lst1

for i in range(0,N):
    ma.append(list(input().strip().split()))
lst = []
for i in range(0,len(ma)):
    if ma[i][0]==address:
        lst.append(ma[i])
        ma=ma[:i]+ma[i+1:]
        break
tem2 = lst[0][2]#下一指针
while tem2 != "-1" or len(ma)!=0:
    ma,tem2,lst = make(ma,tem2,lst)   
    if tem2 == "-1" or len(ma)==0:
        break
out = []
lenth = 0
zu = lst
zup = lst[:K]
num = 0
for i in range(0,len(lst)):
    #每隔k设定为一组数。进行转换操作
    out = tran(zup,K,out)       
    num = (i+1)*K
    zu = zu[num:]
    if num+K>len(lst)-1:
        out  = out + lst[num:]
        break
for i in range(0,len(out)-1):
    out[i][2] = out[i+1][0]
for k in range(0,len(out)):
    print(out[k][0]+" "+out[k][1]+" "+out[k][2],end='\n')


    








