
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        res = []
        if pRoot==None:
            return res
        queue = [pRoot]
        while queue:
            length = len(queue)
            row = []
            for i in queue:
                row.append(i.val)
            res.append(row)
            for i in range(length):
                tmp = queue.pop(0)
                if tmp.left !=None:
                    queue.append(tmp.left)
                if tmp.right !=None:
                    queue.append(tmp.right)
        return res

a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(10)
d = TreeNode(5)
e = TreeNode(7)
f = TreeNode(9)
g = TreeNode(11)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
solution = Solution()
print(solution.Print(a))