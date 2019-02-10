# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 10:07:58 2018

@author: LX

素数对猜想

"""

def isp(a):
    for j in range(2,int(pow(a,0.5)+1)):
        if a%j==0:
            return False
    return True

n = input()
n = int(n)
con,cu = [],0
for i in range(2,n+1):
    if isp(i):
        con.append(i)
for i in range(0,len(con)-1):
    if con[i+1]-con[i]==2:
        cu+=1
print(cu)