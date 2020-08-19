# Definition for a binary tree node.
import sys
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.i = 0

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = self.bst(preorder, float('inf'))
        return root

    def bst(self, A, bound) -> TreeNode:
        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(A[self.i])
        self.i += 1
        root.left = self.bst(A, root.val)
        root.right = self.bst(A, bound)
        return root

    def bstFromArray(self, array: List[int]):
        root = TreeNode(array[0])
        for i in range(1, len(array)):
            ite = root
            while ite:
                if array[i] < ite.val:
                    if not ite.left:
                        ite.left = TreeNode(array[i])
                        break
                    else:
                        ite = ite.left
                if array[i] > ite.val:
                    if not ite.right:
                        ite.right = TreeNode(array[i])
                        break
                    else:
                        ite = ite.right
        return root

if __name__ == '__main__':
    sol = Solution()
    arr = [8, 5, 1, 7, 10, 12]
    print(sol.bstFromPreorder(arr))
    print(sol.bstFromArray(arr))
