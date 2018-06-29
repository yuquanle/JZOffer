

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None and pHead2 == None:
            return None

        if pHead1 == None and pHead2 != None:
            return pHead2

        if pHead1 != None and pHead2 == None:
            return pHead1

        pMerge = ListNode(None)
        pTail = pMerge
        while pHead1 and pHead2:
            p1 = pHead1
            p2 = pHead2
            # 尾插法
            if p1.val <= p2.val:
                pHead1 = pHead1.next
                p1.next = None
                pTail.next = p1
                pTail = p1

            if p2.val < p1.val:
                pHead2 = pHead2.next
                p2.next = None
                pTail.next = p2
                pTail = p2

        if pHead1 != None:
            pTail.next = pHead1
        if pHead2 != None:
            pTail.next = pHead2

        return pMerge.next


a1 = ListNode(1)
b1 = ListNode(4)
c1 = ListNode(9)
a1.next = b1
b1.next = c1

a2 = ListNode(2)
b2 = ListNode(5)
c2 = ListNode(8)
a2.next = b2
b2.next = c2

solution = Solution()
pmerge = solution.Merge(a1, a2)

while pmerge:
    print(pmerge.val)
    pmerge = pmerge.next





