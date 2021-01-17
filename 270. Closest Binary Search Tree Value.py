from DS import TreeNode


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        Idea:
            keep two variables, bigger and smaller,
            update the value as searching the tree
            return the one that is closer to target
        """
        bigger, smaller = float("inf"), -float("inf")
        while root:
            if root.val == target:
                return root.val
            elif root.val > target:
                bigger = min(bigger, root.val)
                root = root.left
            else:
                smaller = max(smaller, root.val)
                root = root.right
        return bigger if bigger - target < target - smaller else smaller
