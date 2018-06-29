

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        root = Solution().ConstructBinaryTree(pre, 0, len(pre)-1, tin, 0, len(tin)-1)
        return root

    def ConstructBinaryTree(self, pre, S1, E1, tin, S2, E2):
        if S1 > E1 or S2 > E2:
            return None

        node = TreeNode(pre[S1])
        index = tin.index(pre[S1])

        node.right = Solution().ConstructBinaryTree(pre, index-S2+S1+1, E1, tin, index+1, E2 )
        node.left = Solution().ConstructBinaryTree(pre, S1+1, index-S2+S1, tin, S2, index-1)

        return node



pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]
solution = Solution()
root = solution.reConstructBinaryTree(pre, tin)

# 层次遍历
list = [root]
while list:
    curruct = list.pop(0)
    print(curruct.val)
    if curruct.left:
        list.append(curruct.left)
    if curruct.right:
        list.append(curruct.right)



