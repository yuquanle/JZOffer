# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead

        reNode = ListNode(None)
        reNode.next = None

        # 头插法
        while pHead:
            p = pHead
            pHead = pHead.next
            p.next = reNode.next
            reNode.next = p
        return reNode.next



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c


solution = Solution()
reNode = solution.ReverseList(a)

# 输出
while reNode:
    if reNode.val != None:
        print(reNode.val)
    reNode = reNode.next



