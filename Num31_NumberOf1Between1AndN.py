
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        sum = 0
        for i in range(1, n+1):
            sum = sum + self.Count_one(i)
        return sum

    def Count_one(self, m):
        if m == 0:
            return 0
        count = 0
        while m:
            n = m % 10
            if n == 1:
                count = count + 1
            m = int (m / 10)
        return count

solution = Solution()
solution.NumberOf1Between1AndN_Solution(13)