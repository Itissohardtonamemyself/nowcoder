# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:41:48 2018

@author: LX

射击游戏

"""


def findre(a1,b1,c1,d1,a2,b2,c2,d2):
    t1 = ((b1-a1)**2)*((b2-a2)**2)
    t2 = ((c1-a1)**2)*((c2-a2)**2)
    t3 = ((d1-a1)**2)*((d2-a2)**2)
    t = min(t1,t2,t3)
    if (t1==t and t2==t) and (t1==t and t3==t) and (t3==t and t2==t) and ((c1-b1)**2)*((c2-b2)**2)==t:
        return True
    else:
        return False

n = input()
n = int(n)
x = list(map(int,input().split()))
y = list(map(int,input().split()))
con=0
for i in range(n):
    a1,b1 = x[i],y[i]
    ta1 = x[:i]+x[i+1:]
    tb1 = y[:i]+y[i+1:]
    for j in range(n-1):
        a2,b2 = ta1[j],tb1[j]
        ta2 = ta1[:j]+ta1[j+1:]
        tb2 = tb1[:j]+tb1[j+1:]
        for k in range(n-2):
            a3,b3 = ta2[k],tb2[k]
            ta3 = ta2[:k]+ta2[k+1:]
            tb3 = tb2[:k]+tb2[k+1:]
            for l in range(n-3):
                a4,b4 = ta3[l],tb3[l]
                ta4 = ta3[:l]+ta3[l+1:]
                tb4 = tb3[:l]+tb3[l+1:]
                if findre(a1,a2,a3,a4,b1,b2,b3,b4):
                    con+=1
                
                
                
                

