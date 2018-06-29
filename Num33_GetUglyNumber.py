
# -*- coding:utf-8 -*-
class Solution:
  def GetUglyNumber_Solution(self, index):
      if index < 7:
          return index
      res = []
      res.append(1)
      t2 = 0
      t3 = 0
      t5 = 0
      for i in range(1, index):
          res.append(min(res[t2]*2,min(res[t3]*3,res[t5]*5)))
          if res[i] == res[t2]*2:
              t2 = t2 + 1
          if res[i] == res[t3]*3:
              t3 = t3 + 1
          if res[i] == res[t5]*5:
              t5 = t5 + 1
      return res[len(res)-1]


solution = Solution()
print(solution.GetUglyNumber_Solution(7))