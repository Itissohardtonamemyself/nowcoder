# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:05:12 2018

@author: LX

Hashing

"""

def issu(a):
    if a==1:
        return False
    else:
        for i in range(2,int(pow(a,0.5)+1)):
            if a%i==0:
                return False
        return True
#def findsu(a):
#    while True:
#        tem = a+1
#        if issu(tem):
#            return tem
#        else:
#            tem+=1
def ori(a):
    global size
    for j in range(0,size):
        if boo[(a+j**2)%size]:
            return (a+j**2)%size
    return -1
m,n = map(int,input().split())
if issu(m):
    size = m
else:
    while issu(m)==False:
        m+=1
    size = m
#    size = findsu(m)
boo = [True for i in range(0,size)]
lst = list(map(int,input().split()))
out = []
for i in lst:
    te = ori(i)
    if te!=-1:
        out.append(str(te))
        boo[te] = False
    else:
        out.append('-')
print(' '.join(out))

#            out.append('-')