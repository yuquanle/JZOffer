

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        odd = []
        even = []
        res = []
        if pRoot == None:
            return None
        if pRoot.left == None and pRoot.right == None:
            res.append([pRoot.val])
            return res


        odd.append(pRoot)
        while odd or even:
            odd1 = []
            while odd:
                tmpodd = odd.pop(0)
                odd1.append(tmpodd.val)
                if tmpodd.left != None:
                    even.append(tmpodd.left)
                if tmpodd.right != None:
                    even.append(tmpodd.right)

            res.append(odd1)
            printlist = []
            even1 = []
            while even:
                tmpeven = even.pop(0)
                printlist.insert(0, tmpeven.val)
                if tmpeven.left != None:
                    odd.append(tmpeven.left)
                if tmpeven.right != None:
                    odd.append(tmpeven.right)

            if printlist:
                for i in printlist:
                    even1.append(i)
                res.append(even1)

        return res


a = TreeNode(8)
# b = TreeNode(6)
# c = TreeNode(10)
# d = TreeNode(5)
# e = TreeNode(7)
# f = TreeNode(9)
# g = TreeNode(11)
# h = TreeNode(8)
# # i = TreeNode(9)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g
# d.left = h
# d.right = i

solution = Solution()
print(solution.Print(a))

