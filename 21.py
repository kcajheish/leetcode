class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
        head = Node(None)
        tail = head
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        if l1:
            tail.next = l1
            tail = tail.next
            l1 = l1.next

        if l2:
            tail.next = l2
            tail = tail.next
            l2 = l2.next

        return head.next

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
    l1 = [1,2,4]
    l2 = [1,3,4]
    expect = [1,1,2,3,4,4]
    s = Solution()
    ll1 = s.arr2ll(l1)
    ll2 = s.arr2ll(l2)
    m_ll = s.mergeTwoLists(ll1, ll2)
    m_arr = s.ll2arr(m_ll)
    assert m_arr == expect
