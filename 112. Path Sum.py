# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        Idea: DFS, as long as it reaches the end, see if the sum equals to the target
        """
        if not root: return False
        def recur(node: TreeNode, add_up: int, target) -> bool:
            # base case, if no children
            if not node.left and not node.right:
                return add_up + node.val == target
            if not node.left:
                return recur(node.right, add_up + node.val, target)
            if not node.right:
                return recur(node.left, add_up + node.val, target)
            return recur(node.right, add_up + node.val, target) or recur(node.left, add_up + node.val, target)

        return recur(root, 0, sum)
