

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False

        # 层次遍历
        queue = []
        queue.append(pRoot1)
        flag = False
        while queue:
            tmpRoot1 = queue.pop()
            # 判断,若相等，则递归
            if tmpRoot1.val == pRoot2.val:
                flag = Solution().doTree1HaveTree2(tmpRoot1, pRoot2)

            if tmpRoot1.left != None:
                queue.append(tmpRoot1.left)
            if tmpRoot1.right != None:
                queue.append(tmpRoot1.right)
        return flag


    def doTree1HaveTree2(self, p1, p2):
        if p2 == None:
            return True
        if p1 == None:
            return False
        if p1.val != p2.val:
            return False
        return Solution().doTree1HaveTree2(p1.left, p2.left) and Solution().doTree1HaveTree2(p1.right, p2.right)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e

b1 = TreeNode(2)
d1 = TreeNode(3)
e1 = TreeNode(5)
b1.left = d1
b1.right = e1

solution = Solution()
print(solution.HasSubtree(a, b1))
