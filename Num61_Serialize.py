

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        if root == None:
            return "#"
        else:
            return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)
    def Deserialize(self, s):
        root, index = self.deserialize(s.split(","), 0)
        return root

    def deserialize(self, s, index):
        if s[index] == '#':
            return None, index + 1

        root = TreeNode(int(s[index]))
        index = index + 1
        root.left, index = self.deserialize(s, index)
        root.right, index = self.deserialize(s, index)
        return root, index


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e

s = "1,2,4,#,#,5,#,#,3,#,#"
solution = Solution()
print(solution.Serialize(a))