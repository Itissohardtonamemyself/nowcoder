# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:46:46 2018

@author: LX

数素数

"""
def ifsu(a):
     for j in range(2,int(pow(a,0.5)+1)):
            if i%j==0:
                return False
     return True

num,lst = 10000,[]
while num>0:
    for i in range(2,9999999):
       if ifsu(i):
           lst.append(i)
           num-=1
           if num==0:
               break
m,n = map(int,input().split())
line = (n-m)//10
yu = (n-m)%10
for i in range(0,line):
    for j in range(m-1+i*10,m+8+i*10):
        print(str(lst[j])+" ",end='')
    print(lst[m+9+i*10-1])
for i in range(m-1+line*10,m-1+line*10+(n-m)%10):
    print(str(lst[i])+" ",end='')
print(lst[n-1])

