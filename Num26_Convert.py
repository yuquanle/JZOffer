# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    InListnode = []
    def Inpost(self, root):
        if root.left != None:
            self.Inpost(root.left)
        self.InListnode.append(root)
        if root.right != None:
            self.Inpost(root.right)

    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return None
        self.InListnode=[]
        self.Inpost(pRootOfTree)
        nodelist = self.InListnode
        for i in range(len(nodelist)-1):
            nodelist[i].right = nodelist[i+1]
            nodelist[i+1].left = nodelist[i]

        pHead = nodelist[0]
        while pHead:
            print(pHead.val)
            pHead = pHead.right



a = TreeNode(6)
b = TreeNode(4)
c = TreeNode(9)
d = TreeNode(3)
e = TreeNode(5)
f = TreeNode(8)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

a1 = TreeNode(6)
b1 = TreeNode(4)
c1 = TreeNode(9)
a1.left = b1
a1.right = c1

solution = Solution()
solution.Convert(a)
solution.Convert(a1)
