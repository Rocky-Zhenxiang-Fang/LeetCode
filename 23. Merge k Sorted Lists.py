from typing import List

from DS import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Idea: From naive approach, we can merge last 2 list node once at a time
            If we change the order, we can see this as a divide and conquer problem
        """
        from collections import deque
        if not lists:
            return None
        que = deque(lists)
        while len(que) > 1:
            for _ in range(len(que) // 2):
                l1 = que.pop()
                l2 = que.pop()
                que.appendleft(self.mergeTwoLists(l1, l2))
        return que[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
        while l1 and l2:
            if l1.val > l2.val:
                ptr.next = l2
                l2 = l2.next
            else:
                ptr.next = l1
                l1 = l1.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2
        return head.next
