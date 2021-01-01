# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList_bad(self, head: 'Node') -> 'Node':
        """
        Idea:
            First, copy the nodes one by one following the next pointer and store the corresponding relationship
            into a heapmap
            Next, iterate again to build the random pointer
        This naive idea takes more memory then necessary
        """
        node_map = {}
        if not head:
            return None
        ptr = head
        while ptr:
            node_map[ptr] = Node(ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr:
            if ptr.next:
                node_map[ptr].next = node_map[ptr.next]
            ptr = ptr.next
        ptr = head
        while ptr:
            if ptr.random:
                node_map[ptr].random = node_map[ptr.random]
            ptr = ptr.next
        return node_map[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Idea: In first iteration, copy each node and attach it to the back of the original node
            The next iteration deal with the random pointer, for each original node that having a random pointer pointing
            at other nodes, its next node will also points at the next node of the random node
            Finally, collect the copied node by reconnecting them
        """
        if not head:
            return None
        ptr = head
        while ptr:
            next_ptr = ptr.next
            ptr.next = Node(ptr.val)
            ptr.next.next = next_ptr
            ptr = next_ptr
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        ptr = head
        res = head.next
        res_ptr = res
        while ptr.next.next and res_ptr.next.next:
            next_ptr = ptr.next.next
            next_res_ptr = res_ptr.next.next
            ptr.next = next_ptr
            res_ptr.next = next_res_ptr
            ptr = ptr.next
            res_ptr = res_ptr.next
        return res