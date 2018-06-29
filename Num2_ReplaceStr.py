# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(" ","%20")


solution = Solution()
print(solution.replaceSpace("We Are Happy"))
