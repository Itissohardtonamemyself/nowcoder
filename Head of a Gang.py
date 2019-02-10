# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:12:32 2018

@author: LX

Head of a Gang

"""

gang = {}
name = {}
index = []
con = 0
n,t = map(int,input().split())
for i in range(n):
    te = input().split()
    if (te[0] not in name) and (te[1] not in name):
        con+=1
        name[te[0]]=[con,int(te[2])]
        name[te[1]]=[con,int(te[2])]
        gang[con]=[int(te[2]),2,te[0],te[1]]      
    elif (te[0] in name) and (te[1] not in name):
        name[te[1]]=[int(name[te[0]][0]),int(te[2])]
        name[te[0]][1]+=int(te[2])
        gang[name[te[0]][0]][0]+=int(te[2])
        gang[name[te[0]][0]][1]+=1
        gang[name[te[0]][0]].append(te[1])
    elif (te[1] in name) and (te[0] not in name):
        name[te[0]]=[int(name[te[1]][0]),int(te[2])]
        name[te[1]][1]+=int(te[2])
        gang[name[te[1]][0]][0]+=int(te[2])###,
        gang[name[te[1]][0]][1]+=1
        gang[name[te[1]][0]].append(te[0])
    elif (te[1] in name) and (te[0] in name) and (name[te[1]][0]==name[te[0]][0]):
        name[te[1]][1]+=int(te[2])
        name[te[0]][1]+=int(te[2])
        gang[name[te[0]][0]][0]+=int(te[2])
    elif (te[1] in name) and (te[0] in name) and (name[te[1]][0]!=name[te[0]][0]):
        name[te[1]][1]+=int(te[2])
        name[te[0]][1]+=int(te[2])
        temp = int(name[te[1]][0])
#        if (name[te[0]][0] in gang) and (name[te[1]][0] in gang):
        gang[name[te[0]][0]][0]+=int(te[2])
        gang[name[te[0]][0]][0]+=int(gang[name[te[1]][0]][0])
        gang[name[te[0]][0]][1]+=int(gang[name[te[1]][0]][1])
        for i in gang[name[te[1]][0]][2:]:
            name[i][0] = int(name[te[0]][0])
            gang[name[te[0]][0]].append(str(i))
        del gang[temp]
#        elif (name[te[0]][0] in gang) and (name[te[1]][0] not in gang):
#            gang[name[te[0]][0]][0]+=int(te[2])
#        elif (name[te[0]][0] not in gang) and (name[te[1]][0] in gang):
#            gang[name[te[1]][0]][0]+=int(te[2])        
outlst = []
for i in gang:
    if gang[i][0]>t and gang[i][1]>2:
        ma = -1
        te = ''
        for j in gang[i][2:]:
            if name[j][1]>ma:
                ma = name[j][1]
                te = j
        outlst.append(te)
print(len(outlst))
outlst.sort()
for i in outlst:
    print(i+" "+str(gang[name[i][0]][1]))