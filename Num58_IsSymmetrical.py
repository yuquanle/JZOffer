

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        def is_same(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val == p2.val:
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False
        if pRoot == None or (pRoot.left==None and pRoot.right==None):
            return True
        if pRoot.left and pRoot.right:
            return is_same(pRoot.left,  pRoot.right)
        return False
