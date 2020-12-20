from DS import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ptr = head
        prev = head
        while ptr:
            if ptr.val != prev.val:
                prev.next = ptr
                prev = prev.next
            ptr = ptr.next
        prev.next = None
        return head