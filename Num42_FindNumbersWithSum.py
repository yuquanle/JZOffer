

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) ==0:
            return []
        i = 0
        t = len(array) - 1
        if array[i] >= tsum:
            return None
        while array[t] >= tsum:
            t = t - 1

        res = []
        while t > i:
            if array[i] + array[t] < tsum:
                i = i + 1
            elif array[i] + array[t] == tsum:
                res.append([array[i],array[t]])
                i = i + 1
                t = t - 1
            else:
                t = t - 1

        mul = 1000000
        if res != []:
            for pair in res:
                if pair[0] * pair[1] < mul:
                    mul = pair[0] * pair[1]
                    x1, x2 = pair[0], pair[1]
            return x1, x2

        return []



solution = Solution()
print(solution.FindNumbersWithSum([],0))


