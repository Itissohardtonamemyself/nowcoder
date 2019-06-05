# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:42:20 2018

@author: LX

Longest Symmetric String

"""

nlst,out = [],0
n = input()
for i in n:
    nlst.append(i)
for i in range(len(nlst)):
    sa1,sa2,j = 0,0,i+1
    while i>=sa1 and i+sa1<len(nlst) and nlst[i-sa1]==nlst[i+sa1]:
        sa1+=1#奇数
    while i>=sa2 and j+sa2<len(nlst) and nlst[i-sa2]==nlst[j+sa2]:
        sa2+=1#偶数
    out = max(out,max(2*sa1-1,2*sa2))
print(out)  

