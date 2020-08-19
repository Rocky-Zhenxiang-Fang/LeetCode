# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycleSlow(self, head: ListNode) -> bool:
        """
        Time Complexity O(n^2)
        Space Complexity O(n)
        """
        ite = head
        past = []
        while ite:
            if ite in past:
                return True
            else:
                past.append(ite)
                ite = ite.next

        return False

    def hasCycle(self, head: ListNode) -> bool:
        """
        Uses two pointers, fast and slow, fast walks twice faster then slow
        if there is no cycle, then the fast pointer will point to None
        if there is a cycle, then the fast pointer will overlap the slow pointer
        Time Complexity O(n)
        Space Complexity O(1)
        """
        if not head or not head.next: return False
        fast = head
        slow = head
        while fast and fast.next:
            if __name__ == '__main__':
                fast = fast.next.next
                slow = slow.next
                if fast is slow:
                    return True
        return False
