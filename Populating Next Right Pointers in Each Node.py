from DS import Node


class Solution(object):
    def connectSlow(self, root):
        """
        Slow
        """
        from collections import deque
        if not root: return root
        de = deque()
        de.append(root)
        while de:
            n = len(de)
            for i in range(n):
                node = de.popleft()
                if i != n - 1:
                    node.next = de[0]
                else:
                    node.next = None
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)
        return root
if __name__ == '__main__':
    [1, 2, 3, 4, 5, 6, 7]
    node7 = Node(7)
    node6 = Node(6)
    node5 = Node(5)
    node4 = Node(4)
    node3 = Node(3, node6, node7)
    node2 = Node(2, node4, node5)
    node1 = Node(1, node2, node3)
    sol = Solution()
    no = sol.connect(node1)

