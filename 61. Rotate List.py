class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    # """
    # redundant iteration, the later two for loops can be merge to one
    # """
    #     if not head: return None
    #     ite = head
    #     size = 1
    #     while ite.next:
    #         size += 1
    #         ite = ite.next
    #
    #     # Now ite is at the last node and the size of ListNode is found
    #     k = k % size
    #     ite.next = head
    #     for _ in range(size - k):
    #         head = head.next
    #     Now, the head is right
    #     endIte = head
    #     for _ in range(size - 1):
    #         endIte = endIte.next
    #     endIte.next = None
    #
    #     return head

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        ite = head
        size = 1
        while ite.next:
            size += 1
            ite = ite.next

        # Now ite is at the last node and the size of ListNode is found
        k = k % size
        ite.next = head
        for _ in range(size - k - 1):
            head = head.next
        end = head
        head = head.next
        end.next = None

        return head
