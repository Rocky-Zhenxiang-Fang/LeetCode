# This file is used to review done questions

# Definition for a binary tree node.
from typing import List

import DS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return TreeNode(0)



if __name__ == '__main__':
    test_head = DS.arr2TreeNode([5,1,4,None,None,3,6])
    sol = Solution()
    print(sol.isValidBST(test_head))
