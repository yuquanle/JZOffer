

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        result = []
        if root == None:
            return result
        stack = []
        stack.append(root)
        while stack != []:
            nodetmp = stack.pop(0)
            result.append(nodetmp.val)
            if nodetmp.left != None:
                stack.append(nodetmp.left)
            if nodetmp.right != None:
                stack.append(nodetmp.right)
        return result



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

solution = Solution()
print(solution.PrintFromTopToBottom(a))