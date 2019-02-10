# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:22:17 2018

@author: LX

函数的魔法

"""

def f(x):
    return (x**3+x**2)%233
def g(x):
    return (x**3-x**2)%233
t = input()
t = int(t)
for i in range(t):
    a,b = map(int,input().split())
    time = 0
    boo = False
    while a!=b:
        a = max(f(a),g(a))
        time+=1
        if time>10000:
            boo = True
    if boo:
        print(-1)
    else:
        print(time)
