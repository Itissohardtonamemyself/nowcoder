# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:59:34 2019

@author: LX

折纸问题

该问题可简化为二叉树。根节点为‘down’.左边是'down',右边是'up'

折了n次，有2**n-1个点

"""

class FoldPaper:
    def foldPaper(self, n):
        res = []
        def fold(n,p):
            if n==0:
                return
            fold(n-1,'left')
            if p=='left':
                res.append('down')
            else:
                res.append('up')
            fold(n-1,'right')
        fold(n,'left')
        return res
               
    
            
        
