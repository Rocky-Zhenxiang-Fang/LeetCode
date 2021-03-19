# Definition for a binary tree node.
import DS
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        Idea:
            For a val that is smaller, it is simple, just add it on the left side
            For a val that is bigger, it could be a right of grandparent, thus, keep a stack of all nodes that are
            lacking of right, when meet a big node, tracback until the last value in stack is bigger then val
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            parent = stack[-1]
            if preorder[i] < parent.val:
                parent.left = TreeNode(preorder[i])
                stack.append(parent.left)
            else:
                while stack and stack[-1].val < preorder[i]:
                    parent = stack.pop()
                parent.right = TreeNode(preorder[i])
                stack.append(parent.right)

        return root




if __name__ == '__main__':
    sol = Solution()
    arr = [8, 5, 1, 7, 10, 12]
    print(sol.bstFromPreorder(arr))
