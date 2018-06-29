# -*- coding:utf-8 -*-
# 回溯法
class Solution:
    def swap(self, cs, i, j):
        temp = cs[i]
        cs[i] = cs[j]
        cs[j] = temp

    def Permutation(self, ss):
        res = []
        ss = list(ss)
        if ss!=None and len(ss)>0:
            self.PermutationHelp(ss, 0, res)
            res.sort()
        return res

    def PermutationHelp(self, cs, i, res):
        if i == len(cs)-1:
            s = "".join(cs)
            if not res.__contains__(s):
                res.append(s)
        else:
            for j in range(i, len(cs)):
                self.swap(cs, i, j)
                self.PermutationHelp(cs, i + 1, res)
                # 交换回来
                self.swap(cs, i, j)

solution = Solution()
solution.Permutation("aa")
