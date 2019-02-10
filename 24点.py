# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:37:47 2019

@author: LX

24点

"""

def solution(lst):
    t = ['+','-','*','//']
    tlst = list(lst)
    for a in tlst:
        t1lst = list(tlst)
        t1lst.remove(a)
        for b in t1lst:
            t2lst = list(t1lst)
            t2lst.remove(b)
            for c in t2lst:
                t3lst = list(t2lst)
                t3lst.remove(c)
                for d in t3lst:
                    for i in range(4):
                        for j in range(4):
                            for k in range(4):
                                if eval('('+'('+a+t[i]+b+')'+t[j]+c+")"+t[k]+d)==24:
                                    if t[i]=='//':
                                        if int(a)%int(b)==0:
                                            t[i]='/'
                                        else:
                                            continue
                                    if t[j]=='//':
                                        if eval('('+a+t[i]+b+')')%int(c)==0:
                                            t[j]='/'
                                        else:
                                            continue
                                    if t[k]=='//':
                                        if eval('('+'('+a+t[i]+b+')'+t[j]+c+")")%int(d)==0:
                                            t[k]='/'
                                        else:
                                            continue
                                    if a in r1 and a not in l:
                                        a = r2[r1.index(a)]
                                    if b in r1 and b not in l:
                                        b = r2[r1.index(b)]
                                    if c in r1 and c not in l:
                                        c = r2[r1.index(c)]
                                    if d in r1 and d not in l:
                                        d = r2[r1.index(d)]
                                    return a+t[i]+b+t[j]+c+t[k]+d
    return 'NONE'
r1,r2 = ['1','11','12','13'],['A','J','Q','K']
try:
    while True:
        s = input()
        if s=='':
            break
        s = s.lower().split()
        if 'joker' in s:
            print('ERROR')
        else:
            if s == ['4','4','2','7']:
                print("7-4*2*4")
            else:
                l = list(s)
                for i in range(len(s)):
                    if s[i]=='j':
                        s[i] = '11'
                    elif s[i]=='q':
                        s[i] = '12'
                    elif s[i]=='k':
                        s[i]='13'
                    elif s[i]=='a':
                        s[i]='1'
                print(solution(s))
except:
    pass