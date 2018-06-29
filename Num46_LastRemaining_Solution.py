

# -*- coding:utf-8 -*-
class Solution:
    # 模拟下标
    def LastRemaining_Solution(self, n, m):
        n_list = []
        for i in range(n):
            n_list.append(i)
        i = -1
        step = -1
        count = n
        while count > 0:
            i = i + 1
            if i >= n:
                i = 0
            if n_list[i] == -1:
                continue
            step = step + 1

            if step == m-1:
                n_list[i] = -1
                step = 0
                count = count - 1

        return i

    # ?
    def LastRemaining_Solution1(self, n, m):
        if n<-1 or m<-1:
            return -1
        n_list = []
        for i in range(n):
            n_list.append(i+1)
        while len(n_list) > 1:
            i = (m - 1 + i) % len(n_list)
            n_list.pop(i)
        return n_list[0]


solution = Solution()
print(solution.LastRemaining_Solution1(5, 3))


