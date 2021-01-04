from LeetCode.DS import TreeNode
import LeetCode.DS as DS


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        idea: do a pre-order traversal, as long as s has value == t, traversal both s and t
        when t is at the end, see if s is also at the end
        if this point is not the root, there might be another root having the same val that is the root, so keep searching
        """
        ans = False
        if not s or not t:
            return False
        if s.val == t.val:
            ans = self.is_same_tree(s, t)
        return ans if ans else self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        else:
            return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)


if __name__ == '__main__':
    sol = Solution()
    test1_1 = DS.arr2TreeNode([3, 4, 5, 1, None, 2])
    test1_2 = DS.arr2TreeNode([3, 1, 2])
    print(sol.isSubtree(test1_1, test1_2))
