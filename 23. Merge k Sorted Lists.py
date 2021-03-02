from typing import List
from DS import ListNode
import collections


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Idea: From naive approach, we can merge last 2 list node once at a time
            If we change the order, we can see this as a divide and conquer problem
        """
        que = collections.deque(lists)
        while len(que) > 1:
            first = que.pop()
            second = que.pop()
            que.appendleft(self.merge2List(first, second))
        return que.pop()

    def merge2List(self, head1: ListNode, head2: ListNode) -> ListNode:
        res = ListNode()
        ptr = res
        while head1 and head2:
            if head1.val < head2.val:
                ptr.next = head1
                head1 = head1.next
            else:
                ptr.next = head2
                head2 = head2.next
            ptr = ptr.next
        if head1:
            ptr.next = head1
        elif head2:
            ptr.next = head2
        return res.next
