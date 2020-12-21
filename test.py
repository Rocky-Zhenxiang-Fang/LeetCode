# This file is used to review done questions



# Definition for a binary tree node.
import DS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Idea: BFS, as long as it ends, return the level
        """
        from collections import deque
        que = deque()
        que.append((root, 1))
        level = 0
        if not root:
            return 0
        while que:
            node, level = que.pop()
            if node.left:
                que.appendleft((node.left, level + 1))
            if node.right:
                que.appendleft((node.right, level + 1))
        return level


if __name__ == '__main__':
    test_head = DS.arr2TreeNode([3, 9, 20, None, None, 15, 7])
    sol = Solution()
    print(sol.maxDepth(test_head))
