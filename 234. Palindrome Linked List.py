# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            fast = fast.next
        # now slow is at the middle of the list, and fast is at the end of the list

        second = slow.next
        slow.next = None
        # now the list has been breck down into head and second

        second = self.reverseList(second)
        # the second has been reversed

        while head and second:
            if head.val != second.val:
                return False
            else:
                head = head.next
                second = second.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        nextNode = head
        currentNode = head
        prevNode = None
        while currentNode.next:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        currentNode.next = prevNode
        head = currentNode
        return head


if __name__ == '__main__':
    node4 = ListNode(1)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    sol = Solution()
    print(sol.isPalindrome(node1))
