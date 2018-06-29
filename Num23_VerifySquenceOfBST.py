# 二叉搜索树，二叉排序树，二叉查找树

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None or sequence == []:
            return False
        if len(sequence) == 1:
            return True

        length = len(sequence)
        i = 0
        root = sequence[-1]
        while sequence[i] < root:
            i = i + 1
        k = i
        for i in range(k,length-1):
            if sequence[i] < root:
                return False

        left_seq = sequence[:k]
        right_seq = sequence[k:length-1]
        Left = True
        Right = True

        if len(left_seq) > 0:
            Left = self.VerifySquenceOfBST(left_seq)
        if len(right_seq) > 0:
            Right = self.VerifySquenceOfBST(right_seq)

        return Left and Right





a = []
solution = Solution()
print(solution.VerifySquenceOfBST(a))

