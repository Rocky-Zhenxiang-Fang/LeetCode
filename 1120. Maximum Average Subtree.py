from typing import Tuple

from DS import TreeNode
import DS


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        """
        Idea:
            Do post_order traversal to get the average and the number of nodes of its sub_trees, then calculate its
            average
        """
        self.max_average = 0
        self.post_order(root)
        return self.max_average

    def post_order(self, node: TreeNode) -> Tuple[float, int]:
        """
        Returns (average, number of nodes)
        """
        if not node:
            return 0, 0
        left_max, left_num, right_max, right_num = 0, 0, 0, 0
        if node.left:
            left_max, left_num = self.post_order(node.left)
        if node.right:
            right_max, right_num = self.post_order(node.right)
        num = left_num + right_num + 1
        average = (left_max * left_num + right_num * right_max + node.val) / num
        self.max_average = max(self.max_average, average)
        return average, num


if __name__ == '__main__':
    r = DS.arr2TreeNode([5, 6, 1])
    sol = Solution()
    print(sol.maximumAverageSubtree(r))
