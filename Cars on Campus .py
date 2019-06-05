# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 23:21:08 2018

@author: LX

Cars on Campus 

"""
def transform(a):
    h1,m1,s1 = map(int,a.split(":"))
    return h1*3600+m1*60+s1
day = [0 for i in range(24*60*60)]
ma,tempcon,concar = 0,0,1
d,d1 = {},{}
tempd,dataout,outcar = [],[],[]
n,k1 = map(int,input().split())
for i in range(n):
    temp = input().split()
    if temp[0] not in d1:
        d1[temp[0]] = [[temp[1],temp[2]]]
    else:
        d1[temp[0]].append([temp[1],temp[2]])
for i in d1:
    d1[i].sort(key=lambda x:(x[0],x[1]))
    k = 0
    tempcon = 0
    while k<len(d1[i])-1:
        if d1[i][k][1]=='in' and d1[i][k+1][1]=='out':
            day[transform(d1[i][k][0])]+=1
            day[transform(d1[i][k+1][0])]-=1
            dataout.append([i,d1[i][k][0],d1[i][k+1][0]])
            h1,m1,s1 = map(int,d1[i][k][0].split(":"))
            h2,m2,s2 = map(int,d1[i][k+1][0].split(":"))
            time = (h2-h1)*3600+(m2-m1)*60+s2-s1
            if i not in d:
                tempcon = time
                d[i] = time
            else:
                tempcon+=time
                d[i] = tempcon
            k+=2
        else:
            k+=1
    if tempcon>ma:
         ma = tempcon
         outcar = [i]
    elif tempcon==ma:
        outcar.append(i)
for i in range(1,24*60*60):
    day[i]+=day[i-1]
#while k1:
#    k1-=1
#    print(day[transform(input())])
try:
    while True:
        lin = input().strip()
        if lin == '':
            break 
        line = lin.split()
        out = []
        for i in line:
            print(day[transform(i)])
except: 
    pass
outcar.sort()
h = ma//3600
m = ma%3600//60
s = ma%60
outcar.append("%02d"%(h)+":"+"%02d"%(m)+":"+"%02d"%(s))
print(" ".join(outcar))

