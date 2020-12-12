from LeetCode.DS import TreeNode
import LeetCode.DS as DS


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        idea: do a pre-order traversal, as long as s has value == t, traversal both s and t
        when t is at the end, see if s is also at the end
        """
        if not s or not t:
            return False

        def isSameTree(s_subtree: TreeNode, t_subtree: TreeNode) -> bool:
            if not s_subtree and not t_subtree:
                return True
            elif not s_subtree or not t_subtree:
                return False
            elif s_subtree.val != t_subtree.val:
                return False
            return isSameTree(s_subtree.left, t_subtree.left) and isSameTree(s_subtree.right, t_subtree.right)

        if s.val == t.val:
            if isSameTree(s, t):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    sol = Solution()
    test1_1 = DS.arr2TreeNode([1, 1])
    test1_2 = DS.arr2TreeNode([1])
    print(sol.isSubtree(test1_1, test1_2))
