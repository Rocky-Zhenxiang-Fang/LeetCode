from DS import ListNode
import DS


class Solution:
    def swapPairs_bad(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        tail = ListNode()
        result = tail
        node_stack = []
        next_node = head
        while next_node:
            node_stack.append(next_node)
            next_node = next_node.next
            if len(node_stack) == 2:
                node_1 = node_stack.pop()
                node_2 = node_stack.pop()
                tail.next = node_1
                node_1.next = node_2
                node_2.next = next_node
                tail = node_2

        return result.next

    def swapPairs(self, head):
        """
        From https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C%2B%2B-Python-Ruby Here,
        pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again,
        a is the current node and b is the next node.
        To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references.
        Instead of thinking about in what order I change them, I just change all three at once.
        """
        result = ListNode()
        pre, pre.next = result, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return result.next


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 3]
    head = DS.arr2LinkedNode(arr)
    head = sol.swapPairs(head)
    DS.print_ListNode(head)
