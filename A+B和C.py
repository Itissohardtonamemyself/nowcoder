# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:15:59 2018

@author: wentong

function:给定区间[-2的31次方, 2的31次方]内的3个整数A、B和C，请判断A+B是否大于C。

"""
t = input()
t = int(t)
lst = []
for i in range(0,t):
    lst.append(list(map(int,input().strip().split())))
for j in range(0,len(lst)):
    a,b,c = lst[j][0],lst[j][1],lst[j][2]
    if a+b>c:
        out = "Case #"+str(j+1)+": true"
    else:
        out = "Case #"+str(j+1)+": false"
    print(out)