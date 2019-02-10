# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:44:31 2018

@author: Build A Binary Search Tree

function:二进制搜索树（BST）递归地定义为二进制树，它具有以下属性：节点的左子树只包含比节点的键少的节点。节点的右子树只包含具有大于
或等于节点的密钥的节点。左、右子树也必须是二叉搜索树。给定二叉树的结构和一系列不同的整数键，只有一个方法可以将这些键填充到树中，
使得生成的树满足BST的定义。样本由图1和图2示出。

每个输入文件包含一个测试用例。对于每种情况，第一行给出一个正整数n（<＝100），它是树中节点总数。
接下来的N行每个都包含“._index right_index”格式的节点的左和右子节点，前提是节点编号从0到N-1，
并且0始终是根。如果缺少一个孩子，那么-1将表示空子指针。最后，在最后一行给出n个不同的整数关键字。

"""

#n = int(input())
#tree = [[] for i in range(n)]
#for i in range(n):
#    tree[i].extend(map(int, input().split()))
#num = sorted(map(int, input().split()))
# 
#inord = []
#def inorder(root):
#    if root!=-1:
#        inorder(tree[root][0])
#        inord.append(root)
#        inorder(tree[root][1])
# 
#lev, cur = [0], [0]
#while cur:
#    chd = [y for x in cur for y in tree[x] if y!=-1]
#    if chd:
#        lev.extend(chd)
#    cur = chd
# 
#inorder(0)
#res = [0 for i in range(n)]
#for i in range(n):
#    res[inord[i]] = num[i]
#ans = [res[x] for x in lev]
#print(' '.join(map(str,ans)))
n = input()
n = int(n)
treelst = []
for i in range(0,n):
    treelst.append(list(map(int,input().split())))
num = list(map(int,input().split()))
num.sort()
inord = []
def inorder(start):
    if start!=-1:
        inorder(treelst[start][0])
        inord.append(start)
        inorder(treelst[start][1])
#backup = list(treelst)   
inorder(0)
lev,cur = [0],[0]
chd = []
while cur:
    for x in cur:
        for y in treelst[x]:
            if y!=-1:
                chd.append(y)
    if len(chd)>0:
        lev.extend(chd)
    cur = list(chd)
    chd = []
res = [0 for i in range(0,n)]
for i in range(0,n):
    res[inord[i]] = num[i]
ans = []
for i in lev:
    ans.append(res[i])
print(" ".join(map(str,ans)))


    
        