

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        for i in range(1, tsum):
            sum = i
            A = []
            A.append(i)
            while sum < tsum:
                i = i + 1
                sum = sum + i
                A.append(i)
            if sum == tsum:
                res.append(A)
        return res


