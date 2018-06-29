

# -*- coding:utf-8 -*-
class Solution:
    stack = []
    def push(self, node):
        Solution().stack.append(node)
    def pop(self):
        if len(Solution().stack) == 0:
            return None
        Solution().stack.pop()
    def top(self):
        if len(Solution().stack) == 0:
            return None
        return Solution().stack[len(Solution().stack)-1]
    def min(self):
        if len(Solution().stack) == 0:
            return None
        m = float('Inf')
        for i in range(len(Solution().stack)):
            if m > Solution().stack[i]:
                m = Solution().stack[i]
        return m

solution = Solution()
solution.push(3)
print(solution.min())
solution.push(4)
print(solution.min())
solution.push(2)
print(solution.min())
solution.push(3)
print(solution.min())
solution.pop()
print(solution.min())
solution.pop()
print(solution.min())
solution.pop()
print(solution.min())
solution.push(0)
print(solution.min())

