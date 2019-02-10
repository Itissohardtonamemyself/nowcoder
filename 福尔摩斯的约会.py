# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:47:56 2018

@author: LX

福尔摩斯的约会

"""

day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
time = '0123456789ABCDEFGHIJKLMN'
s1,s2,s3,s4 = [],[],[],[]
S1 = input()
for i in S1:
    s1.append(i)
S2 = input()
for i in S2:
    s2.append(i)
le = min(len(s1),len(s2))
zimu,index = '',0
for i in range(0,le):
    if s1[i]>='A' and s1[i]<='Z' and s1[i]==s2[i]:
        zimu = s1[i]
        index = i
        break
dayn = ord(zimu)-ord('A')
for i in range(index+1,le):
    if s1[i]==s2[i]:
        shi = time.find(s1[i])
        break
S3 = input()
for i in S3:
    s3.append(i)
S4 = input()
for i in S4:
    s4.append(i)
le = min(len(s3),len(s4))
for i in range(0,le):
    if s3[i]==s4[i] and ((s3[i]>='A' and s3[i]<='Z') or (s3[i]>='a' and s3[i]<='z')) :
        fen = i
        break
print(day[dayn]+" "+"%02d"%shi+":"+"%02d"%fen)
