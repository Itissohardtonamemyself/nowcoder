# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:29:40 2018

@author: LX

成绩排名

"""

n = input()
n = int(n)
gra = []
for i in range(0,n):
    tem = input().split()
    gra.append([tem[0],tem[1],int(tem[2])])
gra.sort(key = lambda x:(x[2]))
print(gra[n-1][0]+' '+gra[n-1][1])
print(gra[0][0]+' '+gra[0][1])