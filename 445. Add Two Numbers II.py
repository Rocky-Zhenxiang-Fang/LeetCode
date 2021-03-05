from DS import ListNode
import DS


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Idea:
            1. Find out the length of each list so that we can align two linkedlist
            2. Add nodes that are in the same level together and reverse it
            3. Deal with the carry
            4. return the reversed linkedlist
        """
        if not l1 and not l2:
            return ListNode()
        if not l1:
            return l2
        if not l2:
            return l1

        # get the size of both linked list
        size_1, size_2 = 0, 0
        ptr_1, ptr_2 = l1, l2
        while ptr_1:
            size_1 += 1
            ptr_1 = ptr_1.next
        while ptr_2:
            size_2 += 1
            ptr_2 = ptr_2.next

        # add nodes that are in the same level
        res = ListNode()
        ptr_1, ptr_2, res_ptr = l1, l2, res
        while size_1 or size_2:
            if size_1 == size_2:
                res_ptr.next = ListNode(ptr_1.val + ptr_2.val)
                ptr_1 = ptr_1.next
                ptr_2 = ptr_2.next
                res_ptr = res_ptr.next
                size_1 -= 1
                size_2 -= 1
            elif size_1 > size_2:
                res_ptr.next = ListNode(ptr_1.val)
                ptr_1 = ptr_1.next
                res_ptr = res_ptr.next
                size_1 -= 1
            else:
                res_ptr.next = ListNode(ptr_2.val)
                ptr_2 = ptr_2.next
                res_ptr = res_ptr.next
                size_2 -= 1
        last = self.reverse_LinkedList(res.next)  # flip the res

        # deal with carry
        carry = 0
        last_ptr = last
        prev = None
        while last_ptr:
            last_ptr.val += carry
            carry = last_ptr.val // 10
            last_ptr.val %= 10
            prev = last_ptr
            last_ptr = last_ptr.next
        if carry:
            prev.next = ListNode(carry)

        return self.reverse_LinkedList(last)

    def reverse_LinkedList(self, head: ListNode) -> ListNode:
        prev = None
        ptr = head
        while ptr:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_node
        return prev


if __name__ == '__main__':
    sol = Solution()
    a = DS.arr2LinkedNode([7, 2, 4, 3])
    b = DS.arr2LinkedNode([5, 6, 4])
    ans = sol.addTwoNumbers(a, b)
    print("Done")
