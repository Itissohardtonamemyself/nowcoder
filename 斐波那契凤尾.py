# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:31:32 2018

@author: LX

function:斐波那契凤尾

"""
fi = [1,1] +[0 for i in range(2,100001)]
for i in range(2,100001):
    fi[i] = (fi[i-1]+fi[i-2])%1000000
fin = [1,1]+[0 for i in range(2,100001)]
i=2
while True:
    fin[i]=fin[i-1]+fin[i-2]
    if fin[i]>999999:
        break
    i+=1
con = -1
for i in fin:
    if i==0:
        break
    else:
        con+=1
try:
    while True:
        n = input()
        n = int(n)
        if n>=30:
            print("%06d"%fi[n])
        else:
            print(fi[n])
except:
    pass

