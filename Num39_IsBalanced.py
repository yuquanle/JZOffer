

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        return max(nLeft+1, nRight+1)



a = TreeNode(8)
b = TreeNode(7)
c = TreeNode(9)
d = TreeNode(6)
e = TreeNode(7.5)
f = TreeNode(8.5)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

solution = Solution()
print(solution.IsBalanced(a))



