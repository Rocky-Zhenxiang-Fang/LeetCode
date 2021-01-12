from DS import Node


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            ans = Node(insertVal)
            ans.next = ans
            return ans
        ptr = head.next
        prev = head
        while ptr != head:
            if prev.val > ptr.val and (insertVal > prev.val or insertVal < ptr.val):
                prev.next = Node(insertVal)
                prev.next.next = ptr
                return head
            elif insertVal == ptr.val or prev.val < insertVal < ptr.val:
                prev.next = Node(insertVal)
                prev.next.next = ptr
                return head
            prev = ptr
            ptr = ptr.next

        # if here, its should be smaller then head or the list is flat
        prev.next = Node(insertVal)
        prev.next.next = ptr
        return head