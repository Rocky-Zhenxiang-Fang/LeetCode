from DS import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Inorder, take out all element, then do a Two sum
        """
        elements = []
        value_map = set()

        def inorder(node):
            if node.left:
                inorder(node.left)
            elements.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        for e in elements:
            if k - e in value_map:
                return True
            else:
                value_map.add(e)
        return False
