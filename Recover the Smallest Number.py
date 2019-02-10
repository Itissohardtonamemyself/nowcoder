# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:24:33 2018

@author: LX

Recover the Smallest Number

"""

#import sys
#n = list(map(str,input().split()))
#nlst = [[] for i in range(0,len(n))]
#ma = -sys.maxsize
#for i in range(0,len(n)):
#    for j in n[i]:
#        nlst[i].append(j)
#    if len(n[i])>ma:
#        ma = len(n[i])
#for i in nlst:
#    if len(i)<ma:
#        i.extend(["0" for j in range(0,ma-len(i))])
#
#nlst.sort(key = lambda x:(x[0]))
#for i in range(0,ma):
#    for j in  range(0,n):
#        if nlst[]


from functools import cmp_to_key
cmp2key = cmp_to_key(lambda x,y: int(x+y)-int(y+x))
print(int(''.join(sorted(input().split()[1:],key=cmp2key))))

