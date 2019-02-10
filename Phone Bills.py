# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:22:40 2018

@author: LX

Phone Bills

"""

def getp(a,b):
    bill = 0
    if b[0]-a[0]>0:
        bill+=(b[0]-a[0])*billday
    if b[1]>=a[1]:
        for i in range(a[1],b[1]):
            bill+=billst[i]*60/100
        bill=bill-billst[a[1]]*a[2]/100+billst[b[1]]*b[2]/100
    else:
        for i in range(0,a[1]):
            bill-=billst[i]*60/100
        for i in range(0,b[1]):
            bill+=billst[i]*60/100
        bill=bill-billst[a[1]]*a[2]/100+billst[b[1]]*b[2]/100
    return bill
         
namelst = {}
name = []
billst = list(map(int,input().split()))
billday = 0
for i in billst:
    billday+=i*60/100
n = input()
n = int(n)
for i in range(n):
    tem = input().split()
    tein = list(map(int,tem[1].split(":")))
    tein.append(tem[2])
    if tem[0] not in namelst:
        namelst[tem[0]] = [tein]
        name.append(tem[0])
    else:
        namelst[tem[0]].append(tein)
name.sort()
mon = "%02d"%(namelst[name[0]][0][0])
for i in name:
    s1 = i+" "+mon
    namelst[i].sort(key=lambda x:(x[1],x[2],x[3]))
    k1,k2 = 0,1
    total=0
    d = []
    while k1<len(namelst[i])-1:
        if namelst[i][k1][4]=='on-line' and namelst[i][k2][4]=='off-line':
            start,end = namelst[i][k1][1:4],namelst[i][k2][1:4]
            startout,endout = [],[]
            for l in start:
                startout.append("%02d"%l)
            for l in end:
                endout.append("%02d"%l)
            s2=":".join(startout)+" "+":".join(endout)+" "
            minute = end[0]*60*24+end[1]*60+end[2]-(start[0]*60*24+start[1]*60+start[2])
            s2+=str(minute)+" "
            price = getp(start,end)
            s2+="$"+"%.2f"%price
            total+=price
            k1+=1
            k2=k1+1
            d.append(s2)
#            if namelst[i][k2][4]=='off-line':
#                end = namelst[i][k2][1:4]
#                startout,endout = [],[]
#                for l in start:
#                    startout.append("%02d"%l)
#                for l in end:
#                    endout.append("%02d"%l)
#                print(":".join(startout)+" "+":".join(endout)+" ",end='')
#                minute = end[0]*60*24+end[1]*60+end[2]-(start[0]*60*24+start[1]*60+start[2])
#                print(str(minute)+" ",end='')
#                price = getp(start,end)
#                print("$"+"%.2f"%price)
#                total+=price
#                k1=int(k2+1)
#                k2=k1+1
#            else:
#                k2+=1
#                if k2>=len(namelst[i]):
#                    k1+=1
#                    k2=k1+1
        else:
            k1+=1
            k2=k1+1
    s3="Total amount: $"+"%.2f"%total
    if d:
        print(s1)
        for q in d:
            print(q)
        print(s3)

