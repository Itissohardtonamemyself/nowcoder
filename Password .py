# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:09:49 2018

@author: wentong

function:Password 

"""

n = input()
n = int(n)
lst = []
for i in range(0,n):
    tem  = list(map(str,input().split()))
    if '1' in tem[1] or '0' in tem[1] or 'l' in tem[1] or 'O' in tem[1]: 
        if '1' in tem[1]:
            tem[1] = tem[1].replace('1','@')
        if '0' in tem[1]:
            tem[1] = tem[1].replace('0','%')
        if 'l' in tem[1]:
            tem[1] = tem[1].replace('l','L')
        if 'O' in tem[1]:
            tem[1] = tem[1].replace('O','o')
        lst.append(tem)
if lst:
    print(len(lst))
    for i in lst:
        print(i[0]+" "+i[1])
elif n>1:
    print("There are " +str(n) +" accounts and no account is modified")
else:
    print("There is 1 account and no account is modified")