from typing import List

from DS import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Idea: postorder always keeps the root at the end
              inorder always keeps the root between subtrees
        """
        if not inorder or len(inorder) != len(postorder):
            return None
        inorder_map = {}  # serves as a cache for faster run time
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def recur(start, end) -> TreeNode:
            """
            returns the root of subtree using inorder[start: end + 1]
            """
            if start > end:
                return None
            sub_root = postorder.pop()
            mid = inorder_map[sub_root]
            curr = TreeNode(sub_root)
            curr.right = recur(mid + 1, end)
            curr.left = recur(start, mid - 1)
            return curr

        return recur(0, len(inorder) - 1)


if __name__ == '__main__':
    inorder = [2, 1]
    postorder = [2, 1]
    sol = Solution()
    print(sol.buildTree(inorder, postorder))
