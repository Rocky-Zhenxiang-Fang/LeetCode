from typing import List

from DS import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        Idea:
            if we recorded the parent of the node, this tree will turn into a graph, then do BFS in range K
        """
        parents = {}
        res = []
        visited = set()

        def preorder(node: TreeNode):
            if node.left:
                parents[node.left] = node
                preorder(node.left)
            if node.right:
                parents[node.right] = node
                preorder(node.right)

        def dfs(node: TreeNode, k):
            if not node or node in visited:
                return
            visited.add(node)
            if k == 0:
                res.append(node.val)
            else:
                dfs(node.right, k - 1)
                dfs(node.left, k - 1)
                dfs(parents.get(node, None), k - 1)
        preorder(root)
        dfs(target, K)
        return res

