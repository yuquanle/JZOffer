
# -*- coding:utf-8 -*-
class Solution:
    sum = 0
    def Sum(self, n):
        self.sum = self.sum + n
        n = n - 1
        return n > 0 and self.Sum_Solution(n)

    def Sum_Solution(self, n):
        self.Sum(n)
        return self.sum

solution = Solution()
print(solution.Sum_Solution(3))