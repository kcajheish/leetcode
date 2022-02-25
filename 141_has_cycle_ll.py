"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false
"""

def arr2ll(arr, pos):
    head = ListNode(arr[0])
    tail = head
    record = None
    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i])
        tail = tail.next
        if pos >= 0 and pos == i:
            record = tail


    if record:
        tail.next = record

    return head

def ll2arr(head):
    visit = set()
    tail = head
    arr = []
    while tail:
        arr.append(tail.val)
        visit.add(tail)
        if tail.next not in visit:
            tail = tail.next
        else:
            break
    return arr

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    """
    time complexity: O(N)
    space complexity: O(N)
    ** how to improve space complexity?
    """
    visited = set()
    while head:
        if head not in visited:
            visited.add(head)
        else:
            return True
        head = head.next
    return False

def hasCycle_slow_fast_pointer(head):
    """
    time complexity: O(N)
    space complexity: O(1)
    idea: if two pointers enter cycle, they meet eventually because of speed difference.
    """
    if not head or not head.next:
        return False

    fast, slow = head, head
    while fast and slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

## follow up: find mid; find entry point of the cycle
def findMid(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def entranceOfCycle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

