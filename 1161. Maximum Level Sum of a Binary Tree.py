class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        Do level order traversal
        After seeing a level, compare its sum to maxSumVal
        If it is bigger, update maxDepth and maxSumVal
        depth += 1
        After visiting all nodes, return maxDepth
        """
        from collections import deque
        q = deque()

        if not root:
            return 0
        maxSumVal = root.val
        maxDepth = 0
        depth = 2
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

        while q:
            count = len(q)
            lvlSum = 0
            for _ in range(count):
                n: TreeNode = q.popleft()
                lvlSum += n.val
                if n.right: q.append(n.right)
                if n.left: q.append(n.left)
            if lvlSum > maxSumVal:
                maxDepth = depth
                maxSumVal = lvlSum
            depth += 1
        return maxDepth

if __name__ == '__main__':
    root1 = TreeNode(-8)
    root2 = TreeNode(7)
    root3 = TreeNode(7, root2, root1)
    root4 = TreeNode(0)
    root5 = TreeNode(1, root3, root4)
    sol = Solution()
    print(sol.maxLevelSum(root5))

