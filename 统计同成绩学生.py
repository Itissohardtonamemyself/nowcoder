# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:16:35 2018

@author: LX

统计同成绩学生

"""

#n = input()
#lst = list(map(int,input().split()))
#cha = list(map(int,input().split()[1:]))
#res = []
#for i in cha:
#    res.append(str(lst.count(i)))
#print(' '.join(res))

tem = list(map(int,input().split()))
lst = tem[1:tem[0]+1]
cha = tem[tem[0]+2:]
res = []
for i in cha:
    res.append(str(lst.count(i)))
print(' '.join(res))