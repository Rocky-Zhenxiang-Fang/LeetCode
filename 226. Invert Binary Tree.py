from DS import TreeNode
import DS


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        idea: recursive call, post order traversal, this gives us the left-sub-tree and the right-sub-tree, switch them, then return the node
        """
        if not root:
            return None
        left_sub_tree, right_sub_tree = None, None
        if root.left:
            left_sub_tree = self.invertTree(root.left)
        if root.right:
            right_sub_tree = self.invertTree(root.right)
        root.left, root.right = right_sub_tree, left_sub_tree
        return root


if __name__ == '__main__':
    test1 = DS.arr2TreeNode([4, 2, 7, 1, 3, 6, 9])
    sol = Solution()
    res = sol.invertTree(test1)
    print(res)
