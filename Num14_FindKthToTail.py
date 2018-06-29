# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        tail = []
        if k <=0 or head == None:
            return None
        while head:
            tail.insert(0, head)
            head = head.next

        if k > len(tail):
            return None
        return tail[k-1]


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

solution = Solution()
print(solution.FindKthToTail(a, 3))
print(solution.FindKthToTail(a, 4))

