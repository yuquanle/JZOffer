# -*- coding:utf-8 -*-
class Solution:
    def findmax(self,tmp):
        if len(tmp)==1:
            return tmp[0]
        flag = tmp[0]
        for i in range(1,len(tmp)):
            if tmp[i]>flag:
                flag = tmp[i]
        return flag

    def maxInWindows(self, num, size):
        res = []
        if size == 0:
            return res
        for i in range(0,len(num)-size+1):
            tmp = num[i:i+size]
            res.append(self.findmax(tmp))
        return res



solution = Solution()
print(solution.maxInWindows([2,3,4,2,6,2,5,1],3))