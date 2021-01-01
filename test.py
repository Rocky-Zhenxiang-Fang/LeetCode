# This file is used to review done questions

# Definition for a binary tree node.
from typing import List, Set
from DS import TreeNode
import DS


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Insight:
            preorder always store the root in front of all its subtrees
            inorder always separate its left subtree and right subtree by its root
        """
        self.next_root = 0
        return self._buildTree_helper(preorder, inorder, 0, len(inorder) - 1)

    def _buildTree_helper(self, preorder: List[int], inorder: List[int], in_start, in_end) -> TreeNode:
        if in_end < in_start or self.next_root >= len(preorder):
            return None
        root = TreeNode(preorder[self.next_root])
        self.next_root += 1
        mid = inorder.index(root.val)
        root.left = self._buildTree_helper(preorder, inorder, in_start, mid - 1)
        root.right = self._buildTree_helper(preorder, inorder, mid + 1, in_end)
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    ans = sol.buildTree(preorder, inorder)
    print(sol.buildTree(preorder, inorder))
    print(" ")
