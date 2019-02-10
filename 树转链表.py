# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:55:52 2019

@author: LX

树转链表

"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Converter:
    h = ListNode(-1)
    o = h
    def treeToList(self, root):
        # write code here
        if root==None:
            return
        self.treeToList(root.left)
        self.o.next = ListNode(root.val)
        self.o = self.o.next
        self.treeToList(root.right)
        return self.h.next