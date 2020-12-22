# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        que = deque()
        res = []
        if not root:
            return res
        que.append(root)
        while que:
            n = len(que)
            sub_res = []
            for _ in range(n):
                curr = que.pop()
                sub_res.append(curr.val)
                if curr.left:
                    que.appendleft(curr.left)
                if curr.right:
                    que.appendleft(curr.right)
            res.append(sub_res)
        return res
