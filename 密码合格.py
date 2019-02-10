# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:40:21 2019

@author: LX

密码合格
"""

try:
    while True:
        s = input()
        if s=='':
            break
        if len(s)<=8:
            print('NG')
        else:
            lst = [0,0,0,0]
            for i in s:
                if i>='A' and i<='Z':
                    lst[0]=1
                elif i>='a' and i<='z':
                    lst[1]=1
                elif i>='0' and i<='9':
                    lst[2]=1
                else:
                    lst[3]=1
            if sum(lst)<3:
                print('NG')
            else:
                boo = True
                for i in range(len(s)-5):
                    for j in range(i+3,len(s)-2):
                        if s[i]==s[j]:
                            if s[i+1]==s[j+1] and s[i+2]==s[j+2]:
                                print('NG')
                                boo = False
                                break
                        if not boo:
                            break
                if boo:
                    print('OK')
except:
    pass