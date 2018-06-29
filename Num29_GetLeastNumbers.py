
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > tinput.__len__():
            return []
        # 先排序
        tinput.sort()
        return tinput[:k]



test = [4, 5, 1, 6, 2, 7, 3, 8]
solution = Solution()
print(solution.GetLeastNumbers_Solution(test, 4))