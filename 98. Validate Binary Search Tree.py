class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array2Tree(arr: [int]) -> TreeNode:
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


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        For a BST, all value of the left-subTree should be smaller then the root;
        all value of the right-subTree should be bigger then the root;
        Thus, for each subTree, we want to store either the minimum value or the maximum value
        and use it to compare to the root's value
        """

    def inOrder(self, root: TreeNode, res):
        if not root:
            return res
        if root.left:
            self.inOrder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inOrder(root.right, res)


if __name__ == '__main__':
    arr = [0, -1]
    root = array2Tree(arr)
    sol = Solution()
    print(sol.isValidBST(root))
