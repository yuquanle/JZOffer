# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, string):
        string = list(string)
        for i in range(len(string)):
            if string[i] == " ":
                string[i] = "%20"
        return "".join(string)

solution = Solution()
print(solution.replaceSpace("I love python"))
print(solution.replaceSpace("We Are Happy"))
