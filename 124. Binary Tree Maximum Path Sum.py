import DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Idea:
            Do a post order, in each level, the maximum path come from taking both legs as long as the sum of leg > 0.
            Return the maximum path that contains itself
        """
        def post_order(node: TreeNode) -> int:
            if not node:
                return 0
            left_val = post_order(node.left)
            right_val = post_order(node.right)
            self.res = max(self.res, node.val + max(0, left_val) + max(0, right_val))
            return node.val + max(0, left_val, right_val)
        self.res = -2000
        post_order(root)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2TreeNode([1, 2, 3])
    root2 = DS.arr2TreeNode([-10, 9, 20, None, None, 15, 7])
    print(sol.maxPathSum(root))
    print(sol.maxPathSum(root2))
