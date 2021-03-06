import collections

from DS import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Idea:
            Do BFS, construct a parent dict, when p and q are both in the parent dict, start backtracking
        """
        parent = {root: (None, 0)}  # stores(node: parent, level)
        que = collections.deque([(root, 0)])
        while que and (p not in parent or q not in parent):
            n = len(que)
            for _ in range(n):
                curr, level = que.pop()
                if curr.left:
                    parent[curr.left] = (curr, level + 1)
                    que.appendleft((curr.left, level + 1))
                if curr.right:
                    parent[curr.right] = (curr, level + 1)
                    que.appendleft((curr.right, level + 1))
        if parent[p][1] > parent[q][1]:  # always make sure that p is higher or equal then q
            p, q = q, p
        while p != q:
            if parent[p][1] == parent[q][1]:    # if both is at the same height
                p = parent[p][0]
                q = parent[q][0]
            else:
                q = parent[q][0]
        return p