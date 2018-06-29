# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == "":
            return -1
        dict = {}
        for i in s:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1

        keylist =[]
        for key in dict:
            if dict[key] == 1:
                keylist.append(key)

        for i in s:
            if keylist.__contains__(i):
                return s.index(i)


solution = Solution()
print(solution.FirstNotRepeatingChar("aaasisiadr"))
