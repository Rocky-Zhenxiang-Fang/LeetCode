class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()  # self.head.next is always the last used node
        self.tail = Node()  # self.tail.prev is always the one need to be delete
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first_node(self, curr: Node) -> None:
        """
        Add a node to self.head.next with Node(key, value)
        """
        old_next = self.head.next
        self.head.next = curr
        curr.prev = self.head
        curr.next = old_next
        old_next.prev = curr

    def remove_last_node(self) -> None:
        """
        Remove self.tail.prev
        """
        if self.tail.prev == self.head:
            return
        real_prev = self.tail.prev.prev
        self.tail.prev = real_prev
        real_prev.next = self.tail

    def remove_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache:
    """
    Idea:
        Naively, using a list and a map. To put the last used element in front will take O(n) time.
            -> Use Linked List
        However, to locate a node in linked list will also take O(n).
            -> Use a map
        However, to move a node in linked list to front also require information for its previous node
            -> Use double linked list
    """

    def __init__(self, capacity: int):
        self.d_linked = DoubleLinkedList()
        self.check = {}     # stores (key: Node)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.check:
            val = self.check[key].val
            new_node = Node(key, val)
            self.d_linked.add_first_node(new_node)
            self.d_linked.remove_node(self.check[key])
            self.check[key] = new_node
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        self.d_linked.add_first_node(new_node)
        if key in self.check:
            self.d_linked.remove_node(self.check[key])
            self.check[key] = new_node
        else:
            self.check[key] = new_node
            if len(self.check) > self.capacity:
                remove = self.d_linked.tail.prev.key
                self.d_linked.remove_last_node()
                del self.check[remove]