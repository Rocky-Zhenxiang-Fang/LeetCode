class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 1
        ite = head
        second = ListNode()
        secIte = second
        lastOdd = None
        while ite:
            if i % 2 == 0:
                lastOdd.next = ite.next
                secIte.next = ite
                secIte = secIte.next
            else:
                lastOdd = ite
            i += 1
            ite = ite.next
        secIte.next = None
        lastOdd.next = second.next
        return head


if __name__ == '__main__':
    node6 = ListNode(6)
    node5 = ListNode(5, )
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    sol = Solution()
    sol.oddEvenList(node1)
    print("Fin")