

# -*- coding:utf-8 -*-
class Solution:
    def FibonacciDigui(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Solution().FibonacciDigui(n-1)+Solution().FibonacciDigui(n-2)

    # 模拟过程
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            list = []
            f1 = 1
            f2 = 1
            list.append(f1)
            list.append(f2)
            for i in range(n):
                f1 = f1 + f2
                list.append(f1)
                if len(list) == n:
                    break
                f2 = f1 + f2
                list.append(f2)
                if len(list) == n:
                    break
        return list[len(list)-1]

solution = Solution()
print(solution.Fibonacci(0))