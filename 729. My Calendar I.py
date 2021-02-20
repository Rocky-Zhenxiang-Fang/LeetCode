class BSTNode:
    def __init__(self, start: int = -1, end: int = -1):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:
    """
    Idea:
        Since we want the event to be sorted and able to lookup, we can create a BST for this
    """

    def __init__(self):
        self.root = BSTNode()

    def book(self, start: int, end: int) -> bool:
        new_event = BSTNode(start, end)
        return self._insert(self.root, new_event)

    def _insert(self, parent: BSTNode, node: BSTNode) -> bool:
        """
        Insert a node to self.root
        :param node: new node to be inserted
        :param parent: current node
        :return: if not double booked, add this leaf and return True, otherwise, return False
        """
        if parent.start <= node.start < parent.end or node.start <= parent.start < node.end:
            return False
        else:
            if parent.start > node.start:
                if not parent.right:
                    parent.right = node
                    return True
                else:
                    return self._insert(parent.right, node)
            else:
                if not parent.left:
                    parent.left = node
                    return True
                else:
                    return self._insert(parent.left, node)


if __name__ == '__main__':
    calender = MyCalendar()
    print(calender.book(10, 20))
    print(calender.book(15, 25))
    print(calender.book(20, 30))








