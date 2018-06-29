

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if len(s)==0:
            return 0
        num = 0
        flag = 1
        length = len(s)-1
        if s[0] == "+":
            while length > 0:
                if not (s[length]>="0" and  s[length]<="9"):
                    return 0
                num = num + flag * int(s[length])
                flag = flag*10
                length = length -1
        elif s[0] == "-":
            while length > 0:
                if not (s[length] >= "0" and s[length] <= "9"):
                    return 0
                num = num + flag * int(s[length])
                flag = flag * 10
                length = length - 1
            num = -num
        else:
            while length >= 0:
                if not (s[length] >= "0" and s[length] <= "9"):
                    return 0
                num = num + flag * int(s[length])
                flag = flag * 10
                length = length - 1
        return num




solution = Solution()
print(solution.StrToInt("123"))