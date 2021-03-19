from DS import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        Idea:
            DFS, keep track of all its grandparents
        """
        res = 0
        stack = [(root, None, None)]    # node, parent, grandparent
        while stack:
            curr, parent, grandparent = stack.pop()
            if grandparent and grandparent.val % 2 == 0:
                res += curr.val
            if curr.left:
                stack.append((curr.left, curr, parent))
            if curr.right:
                stack.append((curr.right, curr, parent))
        return res
