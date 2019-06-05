# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:49:19 2018

@author: wentong

function:Maximum Subsequence Sum 

"""
import sys
k = input()
k = int(k)
lstin = list(map(int,input().split()))
oldsum = lstin[0]
start,end,maxsum = 0,0,-sys.maxsize
for i in range(0,k):
    if oldsum<0:
        start = lstin[i]
        oldsum = 0
    newsum = int(oldsum + lstin[i])
    oldsum = int(newsum)
    if newsum>maxsum:
        maxsum = (newsum)
        end = lstin[i]
        maxstart = int(start)
if maxsum>0:
    print(str(maxsum)+" "+str(maxstart)+" "+str(end))
else:
    print(str(0)+" "+str(lstin[0])+" "+str(lstin[k-1]))

