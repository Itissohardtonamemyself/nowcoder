# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:39:07 2018

@author: LX

function:A+B in Hogwarts

"""
lst = []
a = input()
a = a.strip().split()
for i in a:
    lst.extend(i.strip().split("."))
num = []
for j in lst:
    num.append(int(j))
g1 = int(num[0])
s1 = int(num[1])
k1 = int(num[2])
g2 = int(num[3])
s2 = int(num[4])
k2 = int(num[5])
g3 = int(g1+g2)
s3 = int(s1+s2)
k3 = int(k1+k2)

k31 = int(k3//29)
k3 = k3%29

s3 = k31 + s3
s31 = int(s3//17)
s3 = s3%17
g3 = g3 + s31
print(str(g3)+"."+str(s3)+"."+str(k3))


