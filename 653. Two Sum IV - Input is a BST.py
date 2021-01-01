from DS import TreeNode
import DS


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Idea: do any kind of traversal and store the used number in hashmap
        """
        values = set()

        def preorder(node: TreeNode) -> bool:
            if not node:
                return False
            if k - node.val in values:
                return True
            else:
                values.add(node.val)
                return preorder(node.left) or preorder(node.right)

        return preorder(root)


if __name__ == '__main__':
    sol = Solution()
    r = DS.arr2TreeNode([2, 1, 3])
    k = 3
    print(sol.findTarget(r, k))
