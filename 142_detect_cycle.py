def detectCycle_memo(head):
    visited = set()
    while head:
        if head not in visited:
            visited.add(head)
            head = head.next
        else:
            return head
    return None

def detectCycle_fast_slow(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast