

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = array[0]
        max1 = array[0]
        for i in range(1, len(array)):
            max1 = max(max1+array[i], array[i])
            res = max(max1, res)
        return res


test = [2,8,1,5,9]
solution = Solution()
solution.FindGreatestSumOfSubArray(test)