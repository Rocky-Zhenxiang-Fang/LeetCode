from DS import TreeNode
import DS

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Idea:
            First, find out parent of each node, stop when both p and q are found
            Backtracking from p and q, while p != q, update the deeper one to be its parent
        """
        parent = {root: (root, 0)}  # stores node: (parent, parent's level)
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
            p_parent = parent[p]
            q_parent = parent[q]
            if q_parent[1] < p_parent[1]:
                p = p_parent[0]
            else:
                q = q_parent[0]

        return p


if __name__ == '__main__':
    pass