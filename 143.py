"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

using ds similar to dequeue
https://www.geeksforgeeks.org/deque-in-python/
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reorderList(self, head: Node) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        tail = head
        while tail:
            arr.append(tail)
            tail = tail.next

        tail = Node(None)
        while len(arr) >= 2:
            first = arr.pop(0)
            second = arr.pop(-1)
            first.next = second
            tail.next = first
            tail = second

        if len(arr) == 1:
            tail.next = arr.pop()
            tail = tail.next

        tail.next = None

    def arr2ll(self, arr: list) -> Node:
        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        return head

    def ll2arr(self, head: Node) -> list:
        tail = head
        arr = []
        while tail:
            arr.append(tail.val)
            tail = tail.next
        return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    expect = [1,5,2,4,3]
    s = Solution()
    ll = s.arr2ll(arr)
    s.reorderList(ll)
    print(s.ll2arr(ll))