

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        num_dict = {}
        for i in array:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict.pop(i)
        res = []
        for key in num_dict:
            res.append(key)
        return res


solution = Solution()
print(solution.FindNumsAppearOnce([1,2,3,4,5,6,6,5,4,3]))