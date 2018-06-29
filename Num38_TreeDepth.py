
# 树操作很多都是递归实现
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        treehight = 0
        if pRoot!=None:
            lefthight = self.TreeDepth(pRoot.left)
            righthight = self.TreeDepth(pRoot.right)
            if lefthight >= righthight:
                return lefthight + 1
            else:
                return righthight + 1
        return treehight



root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)

root.left = a
root.right = b
a.left = c
c.left = d

solution = Solution()
print(solution.TreeDepth(root))