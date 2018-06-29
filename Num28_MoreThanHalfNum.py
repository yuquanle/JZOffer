
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        lengh = len(numbers)
        dict = {}
        for i in numbers:
            if not i in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
        for key in dict:
            if dict[key] > lengh/2:
                return key
        return 0

test = [1, 2, 3, 2, 2, 2, 5, 4, 2]
solution = Solution()
print(solution.MoreThanHalfNum_Solution(test))
