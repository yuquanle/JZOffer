# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None

        p = pHead
        while p:
            pcopy = RandomListNode(p.label)
            pcopy.next = p.next
            p.next = pcopy
            p = pcopy.next

        p = pHead
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        randomhead = pHead.next
        pHead.next = None # 不加这句就AC不了
        tmphead = randomhead
        while tmphead.next:
            ptmp = tmphead.next
            tmphead.next = ptmp.next
            tmphead = tmphead.next

        # while randomhead:
        #     print(randomhead.label, randomhead.random.label)
        #     randomhead = randomhead.next

        return randomhead



a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
a.next = b
b.next = c
a.random = c
b.random = c
c.random = b

solution = Solution()
solution.Clone(a)

