from typing import List

from DS import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        Idea:
            if we recorded the parent of the node, this tree will turn into a graph, then do BFS in range K
        """
        parent = {}
        res = []

        def preorder(node: TreeNode):
            if node.left:
                parent[node.left] = node
                preorder(node.left)
            if node.right:
                parent[node.right] = node
                preorder(node.right)

        def bfs(node: TreeNode):
            from collections import deque
            que = deque()
            que.append((node, K))
            visited = set()
            while que:
                curr_node, k = que.pop()
                if curr_node not in visited:
                    visited.add(curr_node)
                    if k == 0:
                        res.append(curr_node.val)
                        continue
                    else:
                        if curr_node.left:
                            que.appendleft((curr_node.left, k - 1))
                        if curr_node.right:
                            que.appendleft((curr_node.right, k - 1))
                        if curr_node in parent:
                            que.appendleft((parent[curr_node], k - 1))
        preorder(root)
        bfs(target)
        return res




