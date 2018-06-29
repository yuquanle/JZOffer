

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        tmpnode = []
        p = pHead
        while p:
            if p in tmpnode:
                return p
            else:
                tmpnode.append(p)
            p = p.next
        return None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = b

solution = Solution()
print(solution.EntryNodeOfLoop(a))