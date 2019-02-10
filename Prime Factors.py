# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:23:10 2018

@author: LX

Prime Factors

"""

n = input()
n = int(n)
backup = int(n)
if n==1:
    print('1=1')
else:
    i = 2
    lst,out = [],[]
#    for i in range(2,int(pow(backup,0.5)+1)):
#        if n%i==0:
#            while n%i==0:
#                lst.append(i)
#                n = n//i
    while n>1:
        if n%i==0:
            lst.append(i)
            n= n//i
        else:
            if i<=n**0.5:
                i+=1
            else:
                i = int(n)
    out = sorted(set(lst))
    print(str(backup)+'=',end='')
    for i in range(0,len(out)-1):
        if lst.count(out[i])>1:
            print(str(out[i])+'^'+str(lst.count(out[i]))+"*",end='')
        else:
            print(str(out[i])+"*",end='')
    if lst.count(out[len(out)-1])>1:
        print(str(out[len(out)-1])+'^'+str(lst.count(out[len(out)-1])))
    else:
        print(str(out[len(out)-1]))




