# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:21:36 2018

@author: LX

The Black Hole of Numbers

"""


nlst,boo = [],True
n = input()
n = int(n)
n = "%04d"%n
 
while True:
    for i in n:
        nlst.append(i)
    n1,n2 = '',''
    nlst.sort()
    for i in nlst:
        n1+=i
    nlst.reverse()
    for i in nlst:
        n2+=i
    if n1==n2:
        boo = False
        print(n1+" - "+n1+" = 0000")
        break
    else:
        n = "%04d"%(int(n2)-int(n1))
        if boo:
            print(n2+" - "+n1+" = "+n)
        nlst = []
        if n=='6174':
           break
