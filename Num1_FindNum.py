# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        col = len(array[0])
        i = row - 1
        j = 0
        while i >= 0 and j < col:
            if target > array[i][j]:
                j = j + 1
            elif target < array[i][j]:
                i = i - 1
            else:
                return True
        return False

solution = Solution()
print(solution.Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))









