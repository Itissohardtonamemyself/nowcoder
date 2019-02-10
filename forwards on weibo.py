# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:42:57 2018

@author: 大佬的答案


"""

n, l = map(int, input().split())
fol = [[] for i in range(n+1)]
for i in range(1, n+1):
    user = list(map(int, input().split()[1:]))
    for u in user:
        fol[u].append(i)
m = list(map(int, input().split()[1:]))
for k in m:
    st = set()
    s = [k]
    ans = 0
    for lev in range(l):    # 层序遍历，用set()统计followers个数
        s = list(set([x for j in s for x in fol[j] if x not in st]))
        st.update(s)
        if k in st: st.remove(k)    # 去除root节点
        ans = len(st)
        if ans == n-1: break
    print(ans)


