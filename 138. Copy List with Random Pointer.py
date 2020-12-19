
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Idea: do a BFS then copy the graph
        Bad memory complexity can be optimized using https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
        """
        ans = head
        if not head:
            return head
        copied = dict()  # stores the (original node: copied node)
        while head:
            if head in copied:  # this means that this node has been created by other random
                copy = copied[head]
            else:
                copy = Node(head.val)
                copied[head] = copy
            if head.next:
                if head.next in copied:
                    copy.next = copied[head.next]
                else:
                    copy.next = Node(head.next.val)
                    copied[head.next] = copy.next
            if head.random:
                if head.random in copied:
                    copy.random = copied[head.random]
                else:
                    copy.random = Node(head.random.val)
                    copied[head.random] = copy.random
            head = head.next
        return copied[ans]



