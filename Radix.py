# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:00:30 2018

@author: wentong

function:Radix

"""

def get(r, L):
    l = len(L); num = 0
    for i in range(l):
        num += L[i]*pow(r,(l-i-1))
    return num

n1,n2,tag,redix = map(str,input().split())
redix = int(redix)
num1,num2=[],[]
for i in n1:
    if i>='0' and i<='9':
        num1.append(int(i))
    else:
        num1.append(ord(i)-87)
for i in n2:
    if i>='0' and i<='9':
        num2.append(int(i))
    else:
        num2.append(ord(i)-87)

#为了方便，我们化为十进制做
if tag=='1':
    #作用于n1
    sn1 = 0
    for i in range(len(num1)-1,-1,-1):
        sn1 = sn1 + num1[i]*pow(redix,len(num1)-1-i)
#    sn2 = 0
    left = max(num2)+1
    right = max(sn1,left)
    isfind = False
    res = 0
    while left<=right:
        mid = (left+right)//2
        temp =get(mid,num2)
        if sn1 == temp:
            res = mid
            isfind = True
            right = mid - 1
        elif sn1<temp:
            right = mid - 1
        else:
            left = mid + 1
    if isfind:
        print(res)
    else:
        print("Impossible")
#    for i in range(0,sys.maxsize):
#        for j in range(len(num2)-1,-1,-1):
#            sn2 = sn2 + num2[j]*pow(i,len(num2)-1-j)
#        if sn2==sn1:
#            print(i)
#            break
#        elif sn2>sn1:
#            print("Impossible")
#            break
#        else:
#            sn2 = 0
else:
    #作用于n2
    sn2 = 0
    for i in range(len(num2)-1,-1,-1):
        sn2 = sn2 + num2[i]*pow(redix,len(num2)-1-i)
#    sn1 = 0
#    for i in range(0,sys.maxsize):
#        for j in range(len(num1)-1,-1,-1):
#            sn1 = sn1 + num1[j]*pow(i,len(num1)-1-j)
#        if sn2==sn1:
#            print(i)
#            break
#        elif sn1>sn2:
#            print("Impossible")
#            break
#        else:
#            sn1 = 0
    left = max(num1)+1
    right = max(sn2,left)
    isfind = False
    res = 0
    while left<=right:
        mid = (left+right)//2
        temp =get(mid,num1)
        if sn2 == temp:
            res = mid
            isfind = True
            right = mid - 1
        elif sn2<temp:
            right = mid - 1
        else:
            left = mid + 1
    if isfind:
        print(res)
    else:
        print("Impossible")









