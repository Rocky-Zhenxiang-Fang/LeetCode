from DS import ListNode
import DS

class Solution:
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


if __name__ == '__main__':
    l_1 = DS.arr2LinkedNode([1, 2, 4])
    l_2 = DS.arr2LinkedNode([1, 3, 4])
    sol = Solution()
    ans = sol.mergeTwoLists(l_1, l_2)
    DS.print_ListNode(ans)

