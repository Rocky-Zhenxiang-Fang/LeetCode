from DS import TreeNode
import DS

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        """
        Idea:
            Do a DFS, collect a path sum when approaching the leaf
            When reach a leaf, we will know if that leaf is sufficient by comparing its path sum with limit
            For any non leaf node, as long as the max_sum of its left and right leg is bigger then limit, then the
            Node is save
        """
        root_path = self._dfs(root, limit, 0)
        return root if root_path >= limit else None

    def _dfs(self, node: TreeNode, limit: int, path_sum: int) -> int:
        current_sum = path_sum + node.val
        if not node.left and not node.right:
            return current_sum
        left = self._dfs(node.left, limit, current_sum) if node.left else -float("inf")
        right = self._dfs(node.right, limit, current_sum) if node.right else -float("inf")
        if left < limit:
            node.left = None
        if right < limit:
            node.right = None
        return max(left, right)


if __name__ == '__main__':
    pass
