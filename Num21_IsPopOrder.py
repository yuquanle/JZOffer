

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop()

        if not len(stack):
            return True
        return False



pushv = [1, 2, 3, 4, 5]
popv = [4, 5, 3, 2, 1]
solution = Solution()
print(solution.IsPopOrder(pushv, popv))