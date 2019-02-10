# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:12:07 2018

@author: LX

Be Unique

"""
#lst = list(map(int,input().split()[1:]))
#r = list(set(lst))
#rong = []
#for i in lst:
#    if r.count(i)>0:
#        rong.append(i)
#        r.remove(i)
#    if len(r)==0:
#        break
#con = 0
#out = None
#for i in rong:
#    if lst.count(i)==1:
#        out = i
#        break
#if out!=None:
#   print(out)
#else:
#   print('None')    
from collections import Counter
lst = list(map(int,input().split()[1:]))
con = Counter(lst)
boo = True
for i in lst:
    if con[i]==1:
        print(i)
        boo = False
        break
if boo:
    print('None')