from DS import TreeNode
import DS


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Idea:
            The maximum distance is length_of_left + length_of_right
        """
        self.res = -float("inf")

        def dfs(node: TreeNode) -> int:
            """
            returns the length of the leg
            """
            if node:
                left_len = dfs(node.left)
                right_len = dfs(node.right)
                self.res = max(self.res, left_len + right_len)
                return 1 + max(left_len, right_len)

            else:
                return 0
        dfs(root)
        return self.res if self.res != -float("inf") else 0


if __name__ == '__main__':
    sol = Solution()
    r = DS.arr2TreeNode([1, 2, 3, 4, 5])
    print(sol.diameterOfBinaryTree(r))
