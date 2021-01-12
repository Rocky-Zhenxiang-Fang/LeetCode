from DS import Node


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Idea:
            Easy way, inorder traversal, store nodes in a array, and then manipulate left and right pointers
            Hard way, during the inorder traversal, we link prev.right = node and node.left = prev. After iterations,
            connect the head and the prev together
        """
        if not root:
            return root
        head = Node(0)  # head.right will be the first node
        prev = head  # prev will stop at the final node

        def inorder(node):
            if not node:
                return
            nonlocal prev
            inorder(node.left)
            prev.right = node
            node.left = prev
            prev = node
            inorder(node.right)

        inorder(root)
        prev.right = head.right
        head.right.left = prev
        return head.right
