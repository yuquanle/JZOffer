

# -*- coding:utf-8 -*-
class Solution:
    def multi(self, A):
        mul = 1
        for i in A:
            mul = mul*i
        return mul

    def multiply(self, A):
        B = []
        for i in range(len(A)):
            tmp = A.pop(i)
            B.append(self.multi(A))
            A.insert(i, tmp)
        return B

solution = Solution()
print(solution.multiply([1, 2, 3, 4, 5]))
