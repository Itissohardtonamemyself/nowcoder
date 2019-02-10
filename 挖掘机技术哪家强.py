# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 10:07:02 2018

@author: wentong

function:输入在第1行给出不超过105的正整数N，即参赛人数。随后N行，每行给出一位参赛者的信息和成绩，包括其所代表的学校的编号、及其比赛成绩（百分制），中间以空格分隔。
在一行中给出总得分最高的学校的编号、及其总分，中间以空格分隔。题目保证答案唯一，没有并列。

"""
n = input()
n = int(n)
lst = []
boo = []
for i in range(0,n):
    lst.append(list(map(int,input().strip().split())))
    boo.append(True)
#tem = lst
he = 0
school = -1
res = []
#lst.sort(key = lambda x :(x[0]))
for i in range(0,len(lst)):
    if boo[i]:
        he = lst[i][1]
        school = lst[i][0]
        for j in range(i+1,len(lst)):
            if lst[i][0]==lst[j][0]:
                he = lst[j][1] + he
                boo[j] = False
        res.append([school,he])
maxres = 0
maxindex = -1
for i in range(0,len(res)):
    if res[i][1]>maxres:
        maxres = res[i][1]
        maxindex = res[i][0]
print(maxindex,maxres)