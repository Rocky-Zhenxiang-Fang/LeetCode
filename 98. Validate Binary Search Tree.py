from DS import *


class Solution:
    def isValidBST_postorder(self, root: TreeNode) -> bool:
        """
        Idea: the subtree of a BST is also a BST
        Do postorder
            for the left subtree, return the biggest value
            for the right subtree, return the smallest value
            If val < left_val or val > right_val:
                return false
        """
        self.flag = True

        def post_order(node: TreeNode):
            """
                returns the (max, min) of a subtree
                """
            if not self.flag: return 0, 0
            left_vals = (-float("inf"), float("inf"))
            right_vals = (-float("inf"), float("inf"))
            if node.left:
                left_vals = post_order(node.left)
            if node.right:
                right_vals = post_order(node.right)
            if node.val <= left_vals[0] or node.val >= right_vals[1]:
                self.flag = False
            return max(right_vals[0], node.val), min(left_vals[1], node.val)

        post_order(root)
        return self.flag

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        """
        Idea: value return using inorder traversal should increase monotonically
        """
        self.last_val = -float("inf")
        self.flag = True

        def in_order(node: TreeNode):
            if self.flag:
                if node.left:
                    in_order(node.left)
                if node.val <= self.last_val:
                    self.flag = False
                else:
                    self.last_val = node.val
                if node.right:
                    in_order(node.right)
        in_order(root)
        return self.flag


if __name__ == '__main__':
    arr = [34, -6, None, -21]
    root = arr2TreeNode(arr)
    sol = Solution()
    print(sol.isValidBST_inorder(root))
