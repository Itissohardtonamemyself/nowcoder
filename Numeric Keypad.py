# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:47:17 2018

@author: LX

Numeric Keypad

"""
lst = [None for i in range(10)]
lst[0]=['0']
lst[1]=['0','1','2','3','4','5','6','7','8','9']
lst[2]=['0','2','3','5','6','8','9']
lst[3]=['3','6','9']
lst[4]=['0','4','5','7','6','8','9']
lst[5]=['0','5','6','8','9']
lst[6]=['6','9']
lst[7]=['0','7','8','9']
lst[8]=['0','8','9']
lst[9]=['9']
lst[0]=['0']
n = input()
n = int(n)
for i in range(n):
    nu = input()
    num = []
    for i in nu:
        num.append(i)
    index = -1
    for i in range(len(num)-1):
        if num[i+1] not in lst[int(num[i])]:
            if num[i+1]>=min(lst[int(num[i])]):
                for k in range(len(lst[int(num[i])])):
                    if lst[int(num[i])][k]>num[i+1]:
                        break
                num[i+1]=lst[int(num[i])][k-1]
                index = i+2
                break
            else:
                te = str(num[i])
                if num[i]!='9' and i>0:
                    num[i] = lst[int(num[i-1])][lst[int(num[i-1])].index(te)-1]
                    index = i+1
                    break
                elif num[i]=='9' and i>0:
                    te = int(i)-1
                    while te>=0 and num[te]=='9':
                        te-=1
                    num[te+1] = str(8)
                    index=te+2
                    break
                elif i==0:
                    num[0] = str(int(num[0])-1)
                    index=1
                    break
    if index!=-1:
        for j in range(index,len(num)):
            num[j] = max(lst[int(num[j-1])])
    out = ''
    for i in num:
        out+=i
    print(out)


