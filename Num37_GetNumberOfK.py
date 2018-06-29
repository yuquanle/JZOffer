

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        count = 0
        for i in data:
            if i < k:
                pass
            if i == k:
                count = count + 1
            if i > k:
                break
        return count


solution = Solution()
print(solution.GetNumberOfK([1,2,3,4,5,6,6,6,7,8],6))
