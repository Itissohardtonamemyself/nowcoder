# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:25:43 2018

@author: LX
"""


nlst = set([])
n = input()
for i in n:
    nlst.add(i)
nlst = sorted(nlst)
for i in range(0,len(nlst)):
    nlst[i] = [nlst[i],str(n.count(nlst[i]))]
for i in nlst:
    print(':'.join(i))