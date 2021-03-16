from DS import ListNode
import DS


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        list_len = 0
        node1 = None
        node2 = None
        ptr = head
        while ptr:
            list_len += 1
            if list_len == k:
                node1 = ptr
            ptr = ptr.next

        k = list_len - k + 1
        ptr = head
        iteration = 0
        while ptr:
            iteration += 1
            if iteration == k:
                node2 = ptr
            ptr = ptr.next

        node1.val, node2.val = node2.val, node1.val
        return head


if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2LinkedNode([1, 2, 3, 4, 5])
    k = 2
    print(sol.swapNodes(root, k))