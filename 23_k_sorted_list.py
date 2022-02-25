'''
https://leetcode.com/problems/merge-k-sorted-lists/
https://www.geeksforgeeks.org/binary-heap/
https://docs.python.org/3/library/heapq.html
'''
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.heap_version(lists)

    def heap_version(self, lists):
        """
        time complexity: flatten K lists, build heap with N nodes, pop N node from min heap
        O(K + N * ln N + N * ln N) ~ O(N * ln N)
        """
        l = []
        for ll in lists:
            while ll:
                heapq.heappush(l, ll.val)
                ll = ll.next

        head = ListNode()
        tail = head
        while l:
            val = heapq.heappop(l)
            tail.next = ListNode(val)
            tail = tail.next
        return head.next

    def list_sort_version(self, lists):
        arr = []
        for ll in lists:
            tail = ll
            while tail:
                arr.append(tail.val)
                tail = tail.next
        arr.sort()
        head = ListNode()
        last = head
        for val in arr:
            last.next = ListNode(val)
            last = last.next

        return head.next