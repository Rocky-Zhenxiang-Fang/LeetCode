# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Idea: To make the tree height balanced, make the root of the tree at the middle of the array
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == '__main__':
    test_arr = [-10, -3, 0, 5, 9]
    sol = Solution()
    head = sol.sortedArrayToBST(test_arr)
    print(head)
