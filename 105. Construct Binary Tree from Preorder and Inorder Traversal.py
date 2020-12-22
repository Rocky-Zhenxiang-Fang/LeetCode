from typing import List
import DS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Idea, preorder: gives the root of left-subtree
              inorder : separates the left sub tree and the right subtree of a given root
        """
        self.root_index = 0
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        def recur(low, high) -> TreeNode:
            if low > high:
                return None
            root = TreeNode(preorder[self.root_index])
            self.root_index += 1
            mid = inorder.index(root.val)
            root.left = recur(low, mid - 1)
            root.right = recur(mid + 1, high)
            return root
        return recur(0, len(preorder) - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    head = sol.buildTree(preorder, inorder)
    print(head.val)
