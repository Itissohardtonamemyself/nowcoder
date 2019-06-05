# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:14:07 2018

@author: LX

Counting Ones

"""

#n = input()
#n = int(n)
#con = 0
#for i in range(1,n+1):
#    tem = str(i)
#    for j in tem:
#        if j=='1':
#            con+=1
#print(con)

n = input()
n = int(n)
res,wei = 0,1
while n//wei:
    h,l,y = n//(wei*10),n//wei%10,n%wei
    res+=h*wei
    if l>1:
        res+=wei
    else:
        if l==1:
            res+=y+1
    wei*=10
print(res)




