"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
"""

from typing import Optional
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        new_head = None
        while head:
            left = head
            right = left.next if left else None
            next = right.next if right else None
            if right:
                right.next = left

            left.next = next

            if prev and right:
                prev.next = right

            if not new_head:
                new_head = right if right else left

            head = next
            prev = left

        return new_head

def make_nodes(arr):
    head = ListNode()
    node = head
    for num in arr:
        next_node = ListNode(num)
        node.next = next_node
        node = node.next
    return head.next

def iterate_nodes(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next
    return results

class TestSwapNode(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        head = self.s.swapPairs(None)
        actual = iterate_nodes(head)
        expect = []
        self.assertEqual(expect, actual)

    def test_odd_node(self):
        head = make_nodes([1,2,3])
        swap_head = self.s.swapPairs(head)
        actual = iterate_nodes(swap_head)
        expect = [2,1,3]
        self.assertEqual(expect, actual)

    def test_even_node(self):
        head = make_nodes([1,2,3,4,5,6])
        swap_head = self.s.swapPairs(head)
        actual = iterate_nodes(swap_head)
        expect = [2,1,4,3,6,5]
        self.assertEqual(expect, actual)

    def test_single_node(self):
        head = make_nodes([2])
        swap_head = self.s.swapPairs(head)
        actual = iterate_nodes(swap_head)
        expect = [2]
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()

