# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def myAddTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Slow, 10% python3 submissions
        """
        head = ListNode()
        ptr1 = l1
        ptr2 = l2
        itr = head

        while ptr1 and ptr2:
            value = ptr1.val + ptr2.val
            itr.next = ListNode(value)
            itr = itr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if ptr1:
            itr.next = ptr1
        elif ptr2:
            itr.next = ptr2

        itr = head
        add = 0
        prev = head
        while itr:
            itr.val += add
            if itr.val >= 10:
                itr.val -= 10
                add = 1
            else:
                add = 0
            prev = itr
            itr = itr.next
        if add != 0:
            prev.next = ListNode(add)
        return head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Faster Solution.
        The idea is the same, but has several optimization
        1. Instead using addition pointers, use l1 and l2 directly instead
        2. If either l1 or l2 is None, assign its value as 0
        """
        head = ListNode()
        itr = head
        add = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1 + v2 + add
            if value >= 10:
                add = 1
                value -= 10
            else:
                add = 0
            itr.next = ListNode(value)
            itr = itr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if add != 0:
            itr.next = ListNode(add)

        return head.next

