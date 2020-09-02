import DS


class Solution(object):
    def __init__(self):
        self.k = 0
        self.ans = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.ans = None
        self.inorder(root)
        return self.ans

    def inorder(self, root):
        if not root or self.ans:
            return
        self.inorder(root.left)
        if self.k == 1:
            self.ans = root.val
            self.k -= 1
            return
        else:
            self.k -= 1
        self.inorder(root.right)


if __name__ == '__main__':
    arr = [5,3,6,2,4,None,None,1]
    r = DS.arr2TreeNode(arr)
    sol = Solution()
    print(sol.kthSmallest(r, 3))