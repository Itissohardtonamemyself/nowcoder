# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:10:30 2018

@author: LX

function:
小红想买些珠子做一串自己喜欢的珠串。卖珠子的摊主有很多串五颜六色的珠串，但是不肯把任何一串拆散了卖。于是小红要你帮忙判断一
下，某串珠子里是否包含了全部自己想要的珠子？如果是，那么告诉她有多少多余的珠子；如果不是，那么告诉她缺了多少珠子。

为方便起见，我们用[0-9]、[a-z]、[A-Z]范围内的字符来表示颜色。例如，YrR8RrY是小红想做的珠串；那么ppRYYGrrYBR2258可以买，因为包含了
全部她想要的珠子，还多了8颗不需要的珠子；ppRYYGrrYB225不能买，因为没有黑色珠子，并且少了一颗红色的珠子。 
    
"""
a = input()
zhu = []
for i in a:
    zhu.append(i)
b = input()
want = []
con = []
coun = 0
for i in b:
    want.append(i)
    con.append(0)
w = list(set(want))
z = list(set(zhu))
conset = [0 for i in range(0,len(w))]
for i in range(0,len(w)):
    for j in z:
        if w[i]==j:
            conset[i] = 1
sumleft = 0
for i in range(0,len(conset)):
    if conset[i] ==1:
         if want.count(w[i])>zhu.count(w[i]):
             sumleft =sumleft + want.count(w[i])-zhu.count(w[i])
sumright = 0
for i in range(0,len(conset)):
    if conset[i] ==0: 
        sumright = sumright + want.count(w[i])

if sum(conset)==len(conset) and sumleft==0:
    print("Yes "+str(len(zhu)-len(want)))
else:
    print("No "+str(sumleft+sumright))