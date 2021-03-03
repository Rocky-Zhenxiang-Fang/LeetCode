from DS import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Idea:
            Construct a parent dict: (node: parent, parent level)
            When backtracking, update the one that is deeper
        """
        parent = {root: (root, 0)}  # assuming that root is its own parent
        stack = [(root, 0)]
        while p not in parent and q not in parent:
            curr, level = stack.pop()
            if curr.left:
                parent[curr.left] = (curr, level)
                stack.append((curr.left, level + 1))
            if curr.right:
                parent[curr.right] = (curr, level)
                stack.append((curr.right, level + 1))
        while p != q:
            p_par, p_level = parent[p]
            q_par, q_level = parent[q]
            if p_level < q_level:
                q = q_par
            else:
                p = p_par

        return p
