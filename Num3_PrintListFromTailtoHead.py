
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        reslut = []
        head = listNode
        while head:
            reslut.insert(0, head.val)
            head = head.next
        return reslut


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c


solution = Solution()
print(solution.printListFromTailToHead(a))