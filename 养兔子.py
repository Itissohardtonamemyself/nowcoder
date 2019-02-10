# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:11:00 2018

@author: LX

养兔子

"""

#1 2 3 5
fi = [1,2]+[0 for i in range(2,91)]
for i in range(2,91):
    fi[i]=fi[i-1]+fi[i-2]
try:
    while True:
        n = input()
        n= int(n)
        print(fi[n-1])
except:
    pass












