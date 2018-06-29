
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        result = ListNode(0)
        res = result
        result.next = pHead
        tmp = pHead
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
            else:
                res.next = tmp
                res = res.next
            tmp = tmp.next
        res.next = tmp
        return result.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g



solution = Solution()
print(solution.deleteDuplication(a))