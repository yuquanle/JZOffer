# -*- coding:utf-8 -*-

'''
思路：利用二维数组从上到下，从左到右递增的规律。
选择左下角元素a[row][col]与target比较，此时有几种情况：
1.当target<=a[row][col]时，此时target一定在a的所在行上面，此时row = row - 1
2.当target>=a[row][col]时，此时target一定在a的所在列右边，此时col = col + 1
3.若不满足1，2且数组没有遍历完，则数组包含target；否则不包含。
'''
class Solution:
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
orderArray = [[1, 2, 8, 9],
              [2, 4, 9, 12],
              [4, 7, 10, 13],
              [6, 8, 11, 15]]
target1 = 5
target2 = 12
print(solution.Find(target1, orderArray))
print(solution.Find(target2, orderArray))









