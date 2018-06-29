

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, root):
        if root != None:
            tmproot = root.left
            root.left = root.right
            root.right = tmproot
            Solution().Mirror(root.left)
            Solution().Mirror(root.right)



