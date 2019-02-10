# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:34:08 2018

@author: LX

继续(3n+1)猜想

"""

def find(a):
    while a>1:
        if a%2==0:
            a = a//2
            res.append(a)
        else:
            a = (3*a+1)//2
            res.append(a)      
def c(t):
  te = []
  for j in t:
        if res.count(j)>0:
            te.append(j)
  if te:
      return te
    
n = input()
n = int(n)
res,out,temp = [],[],[]
lst = list(map(int,input().split()))
if n>1:
    for i in range(0,n):
        find(lst[i])
        tem = lst[:i]+lst[i+1:]
        if c(tem):
            temp.extend(c(tem))
        res = []
    out = sorted(set(lst)-set(temp))
    out.reverse()
    out  = list(map(str,out))
    print(" ".join(out))
else:
    print(lst[0])        





