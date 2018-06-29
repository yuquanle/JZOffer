

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if s == "":
            return ""
        # 移动的位数可能超过字符串的长度
        n = n % len(s)
        s_left = s[:n]
        s = s + s_left
        return s[n:]

solution = Solution()
print(solution.LeftRotateString("abcXYZdef", 3))
