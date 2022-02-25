"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        arr = []
        tail = head
        while tail:
            arr.append(tail)
            tail = tail.next
        remove_node = arr[-n]
        if len(arr) == 1:
            head.val = None
        elif n > 1 and n < len(arr):
            next_node = arr[-n+1]
            prev_node = arr[-n-1]
            remove_node.next = None
            prev_node.next = next_node
        elif n == 1:
            prev_node = arr[-n-1]
            prev_node.next = None
        elif n == len(arr):
            remove_node.next = None

    def arr2ll(self, arr: list) -> Node:
        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        return head

    def ll2arr(self, head: Node) -> list:
        if not head.val:
            return []
        tail = head
        arr = []
        while tail:
            arr.append(tail.val)
            tail = tail.next
        return arr

def test_client(arr, n):
    s = Solution()
    ll = s.arr2ll(arr)
    s.removeNthFromEnd(ll, n)
    result = s.ll2arr(ll)
    print(result)

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = 2
    test_client(arr, n)

    arr = [1]
    n = 1
    test_client(arr, n)

    arr = [1,2]
    n = 1
    test_client(arr, n)
