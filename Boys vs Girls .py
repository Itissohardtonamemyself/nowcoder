# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:26:26 2018

@author: LX

function:Boys vs Girls 

"""

n = input()
n = int(n)
male,female = [],[]
for i in range(0,n):
    tem = list(map(str,input().split()))
    tem[3] = int(tem[3])
    if tem[1]=='M':
        male.append(tem)
    else:
        female.append(tem)
female.sort(key=lambda x:(-x[3]))
male.sort(key=lambda x:(x[3]))

if len(female)!=0 and len(male)!=0:
    defer = int(female[0][3])-int(male[0][3])
else:
    defer = 'NA'
    
if len(male)==0:
    outman = 'Absent'
else:
    del male[0][1]
    male[0].pop()
    outman = ' '.join(male[0])

if len(female)==0:
    outwoman = 'Absent'
else:
    del female[0][1]
    female[0].pop()
    outwoman = ' '.join(female[0])

print(outwoman)
print(outman)
print(defer)