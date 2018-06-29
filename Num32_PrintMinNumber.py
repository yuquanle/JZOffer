

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        str_num = [str(i) for i in numbers]
        for i in range(len(str_num)-1):
            for j in range(i+1,len(str_num)):
                if str_num[i] + str_num[j] > str_num[j] + str_num[i]:
                    tmp = str_num[i]
                    str_num[i] = str_num[j]
                    str_num[j] = tmp

        return "".join(str_num)


test = [3, 323, 32123]
solution = Solution()
print(solution.PrintMinNumber(test))

