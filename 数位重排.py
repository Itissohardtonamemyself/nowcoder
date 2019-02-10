# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:55:09 2018

@author: LX

数位重排

"""

n = input()
n = int(n)
for i in range(n):
    s = input()
    slt = []
    for j in s:
        slt.append(j)
    slt.sort()
    slt.reverse()
    sma = ''
    for j in slt:
        sma+=j
    sma = int(sma)
    if sma%int(s)==0 and sma!=int(s):
        print("Possible")
    else:
        time = sma//int(s)
        boo = True
        for j in range(2,time+1):
            st = str(j*int(s))
            temp = list(slt) 
            for k in st:
                if k in temp:
                    temp.remove(k)
                else:
                    break
            if not temp:
                print("Possible")
                boo = False
                break
        if boo:
            print("Impossible")
            
    