# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        pairscount = 0
        for i in range(0,len(data)-1):
            for j in range(i+1,len(data)):
                if data[i] > data[j]:
                    pairscount = pairscount + 1
        return pairscount % 1000000007



test = [1, 2, 3, 4, 5, 6, 7, 0]
solution = Solution()
print(solution.InversePairs(test))