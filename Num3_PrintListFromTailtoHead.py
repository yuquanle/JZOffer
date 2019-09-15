
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        result = []
        head = listNode
        while head:
            result.insert(0, head.val)
            head = head.next
        return result

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

solution = Solution()
print(solution.printListFromTailToHead(a))