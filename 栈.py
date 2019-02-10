# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:54:06 2018

@author: wentong

function

"""
def getMid(cnt,mid):
    suma = 0
    for i in range(0,len(cnt)):
        suma += count[i]
        if suma>= mid:
            return i
    return 0

n = input()
n = int(n)
stack = []
count = [0 for i in range(0,100000)]
for i in range(0,n):
    line = input()
    if line == 'Pop':
        if len(stack)>0:
            m = stack.pop()
            count[m]-=1
            print(m)
        else:
            print("Invalid")
    elif line == 'PeekMedian':
        if len(stack)>0:
            print(getMid(count,((len(stack)+1)//2)))
        else:
            print("Invalid")
    else:
        lst = list(map(str,line.split()))
        m = int(lst[1])
        stack.append(m)
        count[m]+=1

#分桶只有80%通过率
#def mid():
#    index,cnt =(len(stack)+1)//2,0
#    for i in range(0,size//capi):#先数在哪个桶子里
#        if cnt+count[i]>=index:
#            break
#        cnt += count[i]
#    for j in range(0,capi):#后数在哪个具体位置里
#        cnt += bucket[i][j]
#        if cnt>=index:
#            return j+i*capi
#n = input()
#n = int(n)
#size,capi = 100000,500
#stack = []
#count = [0 for i in range(0,size//capi)]
#bucket = [[0 for i in range(0,capi)] for i in range(0,size//capi)]
#for i in range(0,n):
#    line = input()
#    if line == 'Pop':
#        if len(stack)>0:
#            m = stack.pop()
#            print(m)
#            m-=1
#            bucket[m//capi][m%capi]-=1;
#            count[m//capi]-=1
#        else:
#            print("Invalid")
#    elif line == 'PeekMedian':
#        if len(stack)>0:
#            res = mid()+1
#            print(res)
#        else:
#            print("Invalid")
#    else:
#        lst = list(map(str,line.split()))
#        m = int(lst[1])
#        stack.append(m)
#        m-=1
#        bucket[m//capi][m%capi]+=1
#        count[m//capi]+=1
#线段树 90%通过率
#class zkwsegtree:
#    size = 0
#    T = []
#    def zkw_segtree(ran):
#        zkwsegtree.size = 1
#        while zkwsegtree.size<ran+2:
#            zkwsegtree.size<<=1
#            zkwsegtree.T = [0 for i in range(2*zkwsegtree.size)]
#    def add(value,index):
#        index+=zkwsegtree.size
#        zkwsegtree.T[index]+=value
#        index>>=1
#        while index>0:
#            zkwsegtree.T[index] = zkwsegtree.T[index<<1]+zkwsegtree.T[(index<<1)+1]
#            index>>=1
#            
#    def Query(s,t):
#        ret = 0
#        s+= zkwsegtree.size-1
#        t+=zkwsegtree.size-1
#        while s^t^1:
#            if ~s^1:
#                ret += zkwsegtree.T[s^1]
#            if t^1:
#                ret += zkwsegtree.T[t^1]
#            s +=zkwsegtree.size-1
#            t+=zkwsegtree.size-1
#        return ret
#    def Find_Kth(k,root=1):
#        while (root<<1) < (zkwsegtree.size<<1):
#            if zkwsegtree.T[root<<1]>=k:
#                root = root<<1
#            else:
#                k-=zkwsegtree.T[root<<1]
#                root = (root<<1)+1
#        return root-zkwsegtree.size
#    def azkw_segtree():
#        zkwsegtree.T.clear()
#zkwsegtree.zkw_segtree(100000)
#n = input()
#n = int(n)
#stack = []
#for i in range(0,n):
#    line = input()
#    if line == 'Pop':
#        if len(stack)>0:
#            m = stack.pop()
#            print(m)
#            zkwsegtree.add(-1,m)
#        else:
#            print("Invalid")
#    elif line == 'PeekMedian':
#        if len(stack)>0:
#            print(zkwsegtree.Find_Kth((len(stack)+1)//2))
#        else:
#            print("Invalid")
#    else:
#        lst = list(map(str,line.split()))
#        m = int(lst[1])
#        stack.append(m)
#        zkwsegtree.add(1,m)








