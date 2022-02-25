"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return []
        elif len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])

        return self.merge(l, r)

    def merge(self, l: ListNode, r: ListNode) -> ListNode:
        head = ListNode()
        tail = head
        while l and r:
            if l.val < r.val:
                tail.next = ListNode(l.val)
                l = l.next
            else:
                tail.next = ListNode(r.val)
                r = r.next
            tail = tail.next

        tail.next = l or r
        return head.next

    def arr2ll(self, arr: list) -> ListNode:
        head = ListNode(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = ListNode(arr[i])
            tail = tail.next

        return head

    def ll2arr(self, head: ListNode) -> list:
        tail = head
        arr = []
        while tail:
            arr.append(tail.val)
            tail = tail.next
        return arr
if __name__ == '__main__':
    arrs = [[1,4,5],[1,3,4],[2,6]]
    s = Solution()
    for idx, arr in enumerate(arrs):
        arrs[idx] = s.arr2ll(arr)

    results = s.mergeKLists(arrs)
    print(s.ll2arr(results))