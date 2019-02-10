# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:20:51 2018

@author: LX

Digital Library

"""

n = input()
n = int(n)
tem = [[] for i in range(n)]
for i in range(n):
    for j in range(0,6):
        tem[i].append(input())
tem.sort(key=lambda x:(x[0]))
m = input()
m = int(m)
for i in range(m):
    boo = True
    temp= input()
    print(temp)
    index = int(temp[0])
    temp = temp[3:]
    for j in tem:
        if temp == j[index]:
            print(j[0])
            boo = False
#        elif ' ' in temp:
#            break
        else:
#            boo1 = False
#            for k in j[1:]:
#                klst = list(k.split())
            klst = list(j[index].split())
            for kt in klst:
                if temp == kt:
                    print(j[0])
                    boo = False
#                    boo1 = True
                    break
#            if boo1:
#                break
    if boo:
        print("Not Found")

