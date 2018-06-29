

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Findlen(self, pHead):
        if pHead == None:
            return 0
        len = 0
        while pHead:
            pHead = pHead.next
            len = len + 1
        return len

    def WalkSetp(self, pHead, step):
        while step:
            pHead = pHead.next
            step = step - 1
        return pHead

    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1==None or pHead2==None:
            return None

        len1 = self.Findlen(pHead1)
        len2 = self.Findlen(pHead2)

        if len1 > len2:
            pHead1 = self.WalkSetp(pHead1, len1 - len2)
        else:
            pHead2 = self.WalkSetp(pHead2, len2 - len1)

        while pHead1 !=None:
            if pHead1.val == pHead2.val and pHead1.next==pHead2.next:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None


a1 = ListNode(3)
a2 = ListNode(2)
a3 = ListNode(1)
a4 = ListNode(2)
a5 = ListNode(3)
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5

b1 = ListNode(1)
b2 = ListNode(2)
b3 = ListNode(3)
b1.next=b2
b2.next=b3


solution = Solution()
print(solution.FindFirstCommonNode(a1, b1))


