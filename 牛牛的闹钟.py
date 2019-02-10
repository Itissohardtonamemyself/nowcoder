# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:34:34 2018

@author: LX

牛牛的闹钟

"""

n = input()
n = int(n)
clock = []
for i in range(n):
    h,m = map(int,input().split())
    clock.append(h*60+m)
clock.sort()
walk = input()
walk = int(walk)
geth,getm = map(int,input().split())
time = geth*60+getm
index = -2
for i in range(n):
    if clock[i]>time-walk:
        index = i-1
        break
if index == -2:
    index = n-1
h = clock[index]//60
m = clock[index]%60
print(h,m)