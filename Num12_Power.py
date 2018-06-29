

# -*- coding:utf-8 -*-
class Solution:
    # 考虑所有情况
    def Power(self, base, exponent):
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        result = 1
        for i in range(abs(exponent)):
            result *=base
        if flag == 1:
            return 1 / result
        return result



solution = Solution()
print(solution.Power(2,8))