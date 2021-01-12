# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from DS import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        xs = {}  # stores (x: {y: [vals]})
        res = []

        def preorder(node, x, y):
            if x not in xs:
                xs[x] = {y: [node.val]}
            else:
                y_dict = xs[x]
                y_dict[y] = y_dict.get(y, []) + [node.val]
            if node.left:
                preorder(node.left, x - 1, y - 1)
            if node.right:
                preorder(node.right, x + 1, y - 1)

        preorder(root, 0, 0)
        x_orders = list(sorted(xs.items()))
        for x in x_orders:
            sub = []
            y_orders = list(sorted(x[1].items(), reverse=True))
            for y in y_orders:
                y[1].sort()
                sub = sub + y[1][:]
            res.append(sub)
        return res



