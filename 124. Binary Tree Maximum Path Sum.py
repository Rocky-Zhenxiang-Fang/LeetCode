class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.maxVal = 0

    def dfs(self, node: TreeNode) -> int:
        """
        Used to update self.maxVal
        for a node and its children, the max of its path value is either:
        n.val, n.val + n.left,val, n.val + n.right,val, n.val + n.left,val + n.right.val
        but only the first three can be added to the parent value of n
        thus, we only need to return the max of the first three value to the latest recursion
        :return: max(n.val, n.val + n.left,val, n.val + n.right)
        """
        l, r = None, None
        if node.left:
            l = self.dfs(node.left)
        if node.right:
            r = self.dfs(node.right)

        val = node.val
        lval, rval, lrval = float('-inf'), float('-inf'), float('-inf')
        if l:
            lval = node.val + l
        if r:
            rval = node.val + r
        if l and r:
            lrval = node.val + l + r
        m = max(val, lval, rval)
        self.maxVal = max(m, lrval, self.maxVal)

        return m

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal = root.val

        self.dfs(root)

        return self.maxVal

    def array2Tree(self, arr: [int]) -> TreeNode:
        arrNode: [TreeNode] = [TreeNode()]
        for a in arr:
            if a:
                arrNode.append(TreeNode(a))
            else:
                arrNode.append(None)
        for i in range(1, len(arrNode)):
            if not arrNode[i]:
                continue
            if 2 * i < len(arrNode):
                arrNode[i].left = arrNode[2 * i]
            if 2 * i + 1 < len(arrNode):
                arrNode[i].right = arrNode[2 * i + 1]
        return arrNode[1]


if __name__ == '__main__':
    sol = Solution()
    root = sol.array2Tree([1, 2, 3])
    root2 = sol.array2Tree([-10, 9, 20, None, None, 15, 7])
    print(sol.maxPathSum(root))
    print(sol.maxPathSum(root2))
