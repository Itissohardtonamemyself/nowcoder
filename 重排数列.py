# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:23:09 2018

@author: LX

function:

小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。
牛博士给小易出了一个难题:
对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。
小易现在需要判断一个数列是否可以重排之后满足牛博士的要求。 

于每个数列输出一行表示是否可以满足牛博士要求,如果可以输出Yes,否则输出No
注意 ：print()函数是自带换行的 如果你加了换行符 那就多换了一行了。。。。。

"""
# 020 11
def mathwork(b,k):
    count2 = 0
    count4 = 0
    plus = 0
    for i in range(0,len(b)):
        if b[i]%4 == 0 and b[i]!= 0:
            count4+=1
        elif b[i]%2 == 0 and b[i]!=0:
            count2 +=1
    if count2>1:
        plus = (count4*2+1)+count2
    else:
        plus = count4*2+1
    if plus>=len(b):
        return True
    else:
        return False     
t = input()
t = int(t)
n1 = ''
n = []
a = []
boo = []
output = []
out = ''
for i in range(0,t):
    n1 = input()
    n.append(int(n1))
    a.append(list(map(int,input().strip().split())))
for j in range(0,t):
    boo.append(mathwork(a[j],4))
for k in range(0,len(boo)):
    if boo[k] == True:
        output.append("Yes")
    else:
        output.append("No")
out = output[0]
for i in range(1,len(output)):
    out = out+" "+output[i]
print(out)
