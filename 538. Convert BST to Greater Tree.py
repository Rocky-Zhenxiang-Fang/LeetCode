from DS import TreeNode
import DS


class Solution:
    def convertBST(self, root):
        """
        Idea: Morris In-order Traversal, instead of maintaining a stack of prevs, we use the unused left leg to point
        to the prev node
        """

        def get_next(node: TreeNode) -> TreeNode:
            """
            return the node that is the smallest among all nodes bigger then current node
            """
            next_node = node.right
            while next_node.left and next_node.left is not node:
                next_node = next_node.left
            return next_node

        prev_val = 0
        node = root
        while node:
            if not node.right:
                # no node bigger then current node, add the value to node
                node.val += prev_val
                prev_val = node.val
                node = node.left
            else:
                succ = get_next(node)
                if not succ.left:
                    # this node is not linked before, use the empty left leg to link back to the source
                    succ.left = node
                    node = node.right
                else:
                    # this node has a path to prev node
                    succ.left = None
                    node.val += prev_val
                    prev_val = node.val
                    node = node.left
        return root

    def convertBST_rec(self, root: TreeNode) -> TreeNode:
        """
        Idea:
            Do a reverse inorder traversal, each node.val = node.val + prev_val
        """
        if root:
            self.prev_val = 0
            self.rev_inorder(root)
        return root

    def rev_inorder(self, node):
        if node.right:
            self.rev_inorder(node.right)
        node.val += self.prev_val
        self.prev_val = node.val
        if node.left:
            self.rev_inorder(node.left)


if __name__ == '__main__':
    root = DS.arr2TreeNode([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    sol = Solution()
    sol.convertBST(root)
    print("solved")
