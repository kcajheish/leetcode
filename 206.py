"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from pickle import NONE


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def make_list(self, arr: list) -> ListNode:
        head = ListNode(arr[0])
        end = head
        for i in range(1, len(arr)):
            next_node = ListNode(arr[i])
            end.next = next_node
            end = next_node
        return head

    def make_arry(self, head: ListNode) -> list:
        arr = []
        end = head
        while end is not None:
            arr.append(end.val)
            end = end.next

        return arr

    def reverseList(self, head: ListNode) -> ListNode:
        end = head
        stack = []
        while end is not None:
            stack.append(end.val)
            end = end.next

        reverse_head = ListNode(stack.pop())
        reverse_end = reverse_head

        while len(stack):
            reverse_end.next = ListNode(stack.pop())
            reverse_end = reverse_end.next
        return reverse_head

    def _reverseList(self, head) -> ListNode:
        reverse_head = self._reverseList_helper(None, head)
        return reverse_head

    def _reverseList_helper(self,prev, current) -> ListNode:
        if current.next != None:
            _next = current.next
            current.next = prev
            current = self._reverseList_helper(current, _next)
        else:
            current.next = prev

        return current

    def iterativeReverseList(head):
        """
        time complexity: O(N)
        """
        # the tail of reverse DOES not have next node reference
        prev_node = None

        # if head still has reference to node, keep iterating.
        while head:
            _next = head.next
            head.next = prev_node
            # in next iteration, next node become current head, and head become previous
            prev_node = head
            head = _next
        return prev_node

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    expect = [5,4,3,2,1]
    s = Solution()
    ll = s.make_list(arr)
    reverse_ll = s.reverseList(ll)
    result = s.make_arry(reverse_ll)

    print("iterative reverse list")
    print(result)
    assert result == expect

    reverse_ll = s._reverseList(ll)
    result = s.make_arry(reverse_ll)
    print("recursion reverse list")
    print(result)






# ll = make_list(arr)
# result = make_arry(ll)
# print(result)