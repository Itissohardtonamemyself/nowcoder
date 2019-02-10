# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:53:37 2018

@author: LX

彩色的砖块

"""

s = input()
st = set([])
for i in s:
    st.add(i)
if len(st)>=3:
    print(0)
elif len(st)==2:
    print(2)
else:
    print(1)