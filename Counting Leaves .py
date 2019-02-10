# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:23:50 2018

@author: wentong

function:Counting Leaves 

"""

def find(a):
    if a:
        cnt,con,tem = 0,0,[]
        for j in a:
            for i in lstin:
                if i[0]==j:
                    cnt+=1
                    tem.extend(i[2:])
                    lstin.remove(i)
            if cnt == 0:
                con+=1
            else:
                cnt =0
        count.append(con)
        find(tem)
    else:
        return
                       
n,m = map(int,input().split())
lstin,count = [],[]
for i in range(0,m):
    lstin.append(list(map(int,input().split())))
backup = list(lstin)

root = 1
find([root])
for i in range(0,len(count)):
    count[i] = str(count[i])
print(' '.join(count))
    
