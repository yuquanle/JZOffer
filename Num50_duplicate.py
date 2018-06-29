

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        dict_map = {}
        for i in numbers:
            if not i in dict_map:
                dict_map[i] = 1
            else:
                duplication[0] = i
                return True
        return False

duplication = [0]
solution = Solution()
print(solution.duplicate([2,3,1,0,2,5,3],duplication))
