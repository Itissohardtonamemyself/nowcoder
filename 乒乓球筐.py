# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 10:29:23 2018

@author: LX

乒乓球筐

"""

try:
    while True:
        a,b = map(str,input().split())
        alst,blst,boo = [],[],True
        for i in a:
            alst.append(i)
        for i in b:
            blst.append(i)
        als,bls = sorted(set(alst)),sorted(set(blst))
        for i in range(0,len(bls)):
            if als.count(bls[i])!=0:
                if blst.count(bls[i])>alst.count(bls[i]):
                    boo = False
            else:
                boo = False
        if boo:
            print('Yes')
        else:
            print('No')
except:
    pass





