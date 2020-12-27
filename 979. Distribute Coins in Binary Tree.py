from DS import TreeNode
import DS


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        """
        Idea: for each node, it will either demand one coin or send out multiple coins:
            if node.val == 1:
                it will do nothing
            if node.val == 0:
                it will demand one coin
            else:
                ir will save one coin for itself, and send out all other coins
            Each coins transfer will add one to the result
            Starting from the leaf, which one have one direction, it will send out how many coins that it need or
            it want to sand. For the parent node, it will gather the information from the subtrees and its own value
            then determine its condition based on the previous condition.
        """
        self.res = 0
        self.post_order(root)
        return self.res

    def post_order(self, node: TreeNode) -> int:
        """
        :param node: current node to deal with
        :return: the number of coins needed
        """
        left_condition = 0
        right_condition = 0
        if node.left:
            left_condition = self.post_order(node.left)
        if node.right:
            right_condition = self.post_order(node.right)
        self.res += (abs(left_condition) + abs(right_condition))
        curr_condition = node.val + left_condition + right_condition
        return curr_condition - 1


if __name__ == '__main__':
    root_1 = DS.arr2TreeNode([1, 3, 0, 0, 0, 2, 1])
    sol = Solution()
    print(sol.distributeCoins(root_1))



