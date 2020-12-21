# Definition for a binary tree node.
import DS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        Idea: BFS, return the depth of the first leaf
        """
        from collections import deque
        que = deque()
        if not root:
            return 0
        que.appendleft((root, 1))
        while que:
            curr, depth = que.pop()
            if not curr.left and not curr.right:
                return depth
            if curr.left:
                que.appendleft((curr.left, depth + 1))
            if curr.right:
                que.appendleft((curr.right, depth + 1))
        return -1


if __name__ == '__main__':
    test_head = DS.arr2TreeNode([3, 9, 20, None, None, 15, 7])
    sol = Solution()
    test_head_2 = DS.arr2TreeNode([2, None, 3, None, 4, None, 5, None, 6])
    print(sol.minDepth(test_head))
    print(sol.minDepth(test_head_2))
