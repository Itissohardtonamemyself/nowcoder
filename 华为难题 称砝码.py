# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:08:39 2019

@author: LX

华为难题 称砝码
砝码按重量逐个累加统计

"""
try:
    while True:
        n = input()
        n = int(n)
        m = list(map(int,input().split()))
        x = list(map(int,input().split()))
        st = set([])
        for i in range(x[0]+1):
            st.add(i*m[0])
        for i in range(1,n):
            lst = list(st)
            for j in range(1,x[i]+1):
                for k in range(len(lst)):
                    st.add(lst[k]+j*m[i])
        print(len(st))
except:
    pass
