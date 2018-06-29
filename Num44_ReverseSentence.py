

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        s = s.split(" ")
        i = 0
        e = len(s)-1
        while i < e:
            tmp = s[i]
            s[i] = s[e]
            s[e] = tmp
            i = i + 1
            e = e - 1
        return " ".join(s)

solution = Solution()
print(solution.ReverseSentence("student. a am I"))