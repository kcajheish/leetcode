from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carrier = 0
        head = ListNode()
        current = head
        while l1 or l2:
            accum = carrier
            if l1:
                accum += l1.val
                l1 = l1.next
            if l2:
                accum += l2.val
                l2 = l2.next

            carrier = accum // 10
            num = accum % 10
            current.next = ListNode(val=num)
            current = current.next

        if carrier > 0:
            current.next = ListNode(val=carrier)

        return head.next