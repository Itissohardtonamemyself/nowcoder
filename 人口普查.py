# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:13:47 2018

@author: wentong

function:某城镇进行人口普查，得到了全体居民的生日。现请你写个程序，找出镇上最年长和最年轻的人。
这里确保每个输入的日期都是合法的，但不一定是合理的——假设已知镇上没有超过200岁的老人，而今天是2014年9月6日，所以超过200
岁的生日和未出生的生日都是不合理的，应该被过滤掉。

注意  OJ系统默认以小写字母为输入变量 即 不能写成N=input()，NUM=input() 等等

"""
def rang(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]: #年轻>老 老的往前排
                a[j],a[j+1] = a[j+1],a[j]
                lst[j],lst[j+1] = lst[j+1],lst[j]

def quchu(lst1):
    for i in range(0,len(lst1)):
        if i>len(lst1)-1:
            break
        else:
            if lst1[i][1] >Y:
                if i ==len(lst1)-1:
                    lst1.pop()
                    quchu(lst1)   
                    if i>len(lst1)-1:
                        break
                else:
                    lst1.remove(lst1[i])
            elif lst1[i][1]==Y and lst1[i][2] > M:
                 if i ==len(lst1)-1:
                    lst1.pop()
                    quchu(lst1)   
                    if i>len(lst1)-1:
                        break
                 else:
                    lst1.remove(lst1[i])
            elif lst1[i][1]==Y and lst1[i][2]==M and lst1[i][3]>D:
                 if i ==len(lst1)-1:
                    lst1.pop()
                    quchu(lst1)  
                    if i>len(lst1)-1:
                         break
                 else:
                    lst1.remove(lst1[i])
            if Y - lst1[i][1]>200:
                 if i ==len(lst1)-1:
                    lst1.pop()
                    quchu(lst1)     
                    if i>len(lst1)-1:
                        break
                 else:
                    lst1.remove(lst1[i])
            elif Y - lst1[i][1]==200 and lst1[i][2]<M:
                if i ==len(lst1)-1:
                    lst1.pop()
                    quchu(lst1)  
                    if i>len(lst1)-1:
                        break
                else:
                    lst1.remove(lst1[i])
            elif Y - lst1[i][1] == 200 and lst1[i][2]==M and lst1[i][3]<D:
                if i ==len(lst1)-1:
                    lst1.pop()
                    quchu(lst1)   
                    if i>len(lst1)-1:
                         break
                else:
                    lst1.remove(lst1[i])
    return lst1
n = int(input())
a = []
lst = []
Y = 2014
M = 9
D = 6
for i in range(0,n):
    b = []
    a = input().strip().split("/")
    b = a[0].split(" ")
    for j in range(1,len(a)):
        b.append(a[j])
    lst.append(b)
for j in range(0,len(lst)):
    lst[j][1],lst[j][2],lst[j][3] = int(lst[j][1]),int(lst[j][2]),int(lst[j][3])
lst = quchu(lst)
year = []
month = []
day = []
tem = 0
for k in range(0,len(lst)):
    year.append(lst[k][1])
rang(year)
for k in range(0,len(lst)):  #找出年中并列的排月
    tem = lst[k][1]
    month.append(tem)
    for k1 in range(k+1,len(lst)):
        if tem == lst[k1][1]:
            month.append(lst[k1][1])
    if len(month)>1:
        rang(month)
    month = []
for k in range(0,len(lst)):  #找出月中并列的排日
    tem = lst[k][2]
    day.append(tem)
    for k1 in range(k+1,len(lst)):
        if tem == lst[k1][2]:
            day.append(lst[k1][2])
    if len(day)>1:
        rang(day)
    day = []
length = len(lst)
old = lst[0][0]
young = lst[len(lst)-1][0]
print(str(length)+" "+old+" "+young)

