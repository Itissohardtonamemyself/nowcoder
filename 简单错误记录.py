# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:32:01 2019

@author: LX

简单错误记录

"""
out,namelst = [],{}
try:
    while True:
        s = input()
        s = s.split()
        if ':' in s[0]:
              lst = s[0].split('\\')
              name = lst[-1]
        else:
            name = s[0]
            lst = []
        nst = name+s[1]
        if nst not in namelst:
            namelst[nst] = 1
        else:
            namelst[nst] += 1
        if len(name)>16:
            nam = name[-16:]
        else:
            nam = name
        boo  =True
        for i in range(len(out)):
            if out[i][1]==nst:
                out[i][0] = nam+' '+s[1]+' '+str(namelst[nst])
                boo = False
                break
        if boo:
            out.append([nam+' '+s[1]+' '+str(namelst[nst]),nst])
except:
    pass
if len(out)>8:
    out = out[-8:]
for i in out:
    print(i[0])