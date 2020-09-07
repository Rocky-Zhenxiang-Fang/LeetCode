from DS import TreeNode
import DS


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return root
        self.res = root

        def inorder(node, prev):
            if not node: return
            inorder(node.left, node)
            if node.val < L:
                node = node.right
            if node.val > R:
                node = node.left
            inorder(node.right, node)
        inorder(root, None)
        return self.res


if __name__ == '__main__':
    arr = [3,2,4,1]
    root = DS.arr2TreeNode(arr)
    node0 = TreeNode(0)
    node2 = TreeNode(2)
    node1 = TreeNode(1, node0, node2)
    sol = Solution()
    print(sol.trimBST(root, 1, 1))
    print("S")
