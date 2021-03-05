from DS import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Idea:
            Find the first node that is in between p and q
        """
        if p.val < q.val:  # makes p.val >= q.val
            p, q = q, p

        while root:
            if q.val <= root.val <= p.val:
                return root
            elif root.val < q.val:
                root = root.right
            else:
                root = root.left
        return TreeNode()
