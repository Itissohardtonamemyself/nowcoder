# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:23:45 2018

@author: LX

1098. Insertion or Heap Sort

"""

#不需要写出排序算法 模拟过程即可
from collections import deque
def swap_param(dlstin, i, j):
    dlstin[i], dlstin[j] = dlstin[j], dlstin[i]
    return dlstin
def heap_adjust(dlstin, start, end):
    temp = dlstin[start]
    i = start
    j = 2*i
    while j <= end:
        if (j < end) and (dlstin[j] < dlstin[j + 1]):
            j += 1
        if temp < dlstin[j]:
            dlstin[i] = dlstin[j]
            i = j
            j = 2*i
        else:
            break
    dlstin[i] = temp
def heap_sort(a):
    global dlstin
    en = len(a)-1
    st = en//2
    for i in range(st):
        heap_adjust(a,st-i,en)
    for i in range(en - 1):
        dlstin = swap_param(dlstin, 1, en - i)
        heap_adjust(dlstin, 1, en - i - 1)
        te = list(dlstin)
        if te[1:] not in lsth:
            lsth.append(te[1:])

def insert_sort(a):
    for i in range(0,len(a)):
        tem = a[:i+1]
        tem.sort()
        if tem+a[i+1:] not in lsti:
            lsti.append(tem+a[i+1:])
n = input()
n = int(n)
lsti,lsth = [],[]
lstin = list(map(int,input().split()))
insert_sort(lstin)
dlstin = deque(lstin)
dlstin.appendleft(0)
heap_sort(dlstin)
lstt=  list(map(int,input().split()))
if lstt in lsti:
    print("Insertion Sort")
    con = lsti.index(lstt)
    print(" ".join(map(str,lsti[con+1])))
else:
    print("Heap Sort")
    con = lsth.index(lstt)
    print(" ".join(map(str,lsth[con+1])))

