# Definition for singly-linked list.
from DS import ListNode
import DS

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        The ListNode can be divided into two halves, assuming it is A and B
        The size of the ListNode = n
        A = L1 -> L2 -> L3 -> ... -> L_n
        B = L_n+1 -> ... -> L_n
        We can reverse B, and then merge to lists
        This approach can be modified: https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained
        1. Instead of iterating twice to get the middle point, it can be done using two pointers, fast = slow * 2.
            When fast reaches the end, slow is in the middle
        """
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            prev.next = None
            slow = self._reverse(slow)
            self._merge(head, slow)

    def _reverse(self, head: ListNode) -> ListNode:
        prev = None
        ptr = head
        while ptr:
            ptr_next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = ptr_next
        return prev

    def _merge(self, head1: ListNode, head2: ListNode):
        res = ListNode()
        ptr = res
        while head1 and head2:
            ptr.next = head1
            head1 = head1.next
            ptr.next.next = head2
            head2 = head2.next
            ptr = ptr.next.next
        ptr.next = head2


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4]
    first = DS.arr2LinkedNode(arr)
    second = DS.arr2LinkedNode(arr2)
    sol = Solution()
    sol.reorderList(first)
    print(first)
