

# -*- coding:utf-8 -*-
class Solution:
    # 二进制数，每一减1与自己求交集会少1
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xFFFFFFFF #把负号去掉，如果负号在后面会陷入死循环
       # print(bin(n))
        while n != 0:
            n = n & (n - 1)
            count = count + 1
        return count


solution = Solution()
print(solution.NumberOf1(-5))
