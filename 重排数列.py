# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 23:45:41 2018

@author: LX

重排数列

"""



t = input()
t = int(t)
for k in range(t):
    n = input()
    n = int(n)
    con4,con2 = 0,0
    lst = list(map(int,input().split()))
    for i in range(n):
        if lst[i]%4==0:
            con4+=1
        elif lst[i]%2==0:
            con2+=1
    if con2==1:
        con2=0
    if n%2==0:
        if con4*2+con2>=n:
            print("Yes")
        else:
            print("No")
    else:
        if con4*2+con2>=n-1:
            print("Yes")
        else:
            print("No")
