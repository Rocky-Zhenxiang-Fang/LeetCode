# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def array2ListNode(cls, arr):
        nodeArr = []
        for i in range(len(arr)):
            nodeArr.append(ListNode(arr[i]))

        for i in range(len(arr) - 1):
            nodeArr[i].next = nodeArr[i + 1]
        return nodeArr[0]


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
        import math
        if not head or not head.next or not head.next.next:
            return
        ite = head
        size = 1
        while ite.next:
            size += 1
            ite = ite.next
        # Now we have the size
        ite = head
        for _ in range(math.ceil(size / 2) - 1):
            ite = ite.next
        B = ite.next
        ite.next = None
        second = self.reverse(B)
        self.merge(head, second)

    def reverse(self, node: ListNode) -> ListNode:
        """
        reverse a list of node in place
        """
        prev = None
        current = node
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def merge(self, main: ListNode, sec: ListNode) -> None:
        """
        merges sec into main in the sequence of
        m0 -> s0 -> m1 -> s1 ...
        """
        ite = main
        mainTemp = main
        secTemp = sec
        flag = 0
        while mainTemp and secTemp:
            if flag == 0:
                mainTemp = mainTemp.next
                ite.next = secTemp
            else:
                secTemp = secTemp.next
                ite.next = mainTemp
            flag ^= 1
            ite = ite.next


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4]
    first = ListNode.array2ListNode(arr)
    second = ListNode.array2ListNode(arr2)
    sol = Solution()
    sol.reorderList(second)
    print(first)
