

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if len(array) <= 1:
            return array
        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                odd.append(array[i])
            else:
                even.append(array[i])
        odd.extend(even)
        return odd


a = [1,2,3,4,5,6]
solution  = Solution()
print(solution.reOrderArray(a))


