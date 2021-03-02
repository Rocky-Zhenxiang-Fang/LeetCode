from DS import ListNode
import DS
from typing import Tuple


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Idea:
            Make a function to reverse ListNode from start to end and return the head and tail after reverse
            Call the function between k nodes
            Use iteration to prevent using extra memory
        """
        if k == 1:
            return head

        def reverse(start: ListNode, end: ListNode) -> Tuple[ListNode, ListNode]:
            p = start
            pv = ListNode()
            while p and pv != end:
                ne = p.next
                p.next = pv
                pv = p
                p = ne

            return end, start

        res = ListNode()
        res.next = head
        prev = res
        ptr = head
        depth = 0
        while ptr:
            if depth == k - 1:
                n = ptr.next
                head, tail = reverse(prev.next, ptr)
                prev.next = head
                tail.next = n
                prev = ptr
                ptr = n
                depth = 0

            else:
                ptr = ptr.next
                depth += 1

        return res.next


if __name__ == '__main__':
    sol = Solution()
    head = DS.arr2LinkedNode([1, 2, 3, 4, 5])
    k = 2
    print(sol.reverseKGroup(head, k))

