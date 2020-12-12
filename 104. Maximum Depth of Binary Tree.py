from collections import deque

from LeetCode.DS import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        depth = 0

        que = deque([root])
        while que:
            n = len(que)
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth += 1

        return depth
