
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.res = []
        self.Midtraverse(pRoot)
        if pRoot == None or len(self.res)<k or k == 0:
            return None

        return self.res[k-1]

    def Midtraverse(self, pRoot):
        if pRoot == None:
            return None

        self.Midtraverse(pRoot.left)
        self.res.append(pRoot)
        self.Midtraverse(pRoot.right)

a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(3)
d = TreeNode(4.5)
e = TreeNode(6)

a.left = b
a.right = e
b.left = c
b.right = d

solution = Solution()
print(solution.KthNode(a, 3))