# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:44:29 2018

@author: LX

Count PAT's

"""

con1,con2,con3 = 0,0,0
n = input()
for i in n:
    if i=='P':
        con1+=1
    if i=='A':
        con2+=con1
    if i=='T':
        con3+=con2
print(con3%1000000007)
    

