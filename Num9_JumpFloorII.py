

# -*- coding:utf-8 -*-
class Solution:
    # 排列组合
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        else:
            return 2 ** (number-1)



solution = Solution()
print(solution.jumpFloorII(3))