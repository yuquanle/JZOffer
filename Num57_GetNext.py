
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            res = pNode.right
            while res.left:
                res = res.left
            return res

        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
        return None


a = TreeLinkNode(1)
b = TreeLinkNode(2)
c = TreeLinkNode(3)
d = TreeLinkNode(4)
e = TreeLinkNode(5)

a.left = b
a.right = c
b.left = d
b.right = e

solution = Solution()
print(solution.GetNext(a))