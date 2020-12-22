from typing import List
import DS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        left = True
        res = []
        de = deque()
        de.append(root)
        while de:
            n = len(de)
            sub = deque()
            while n > 0:
                node = de.popleft()
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)
                if left:
                    sub.append(node.val)
                else:
                    sub.appendleft(node.val)
                n -= 1
            left = not left
            res.append(list(sub))

        return res


if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None,None,15,7])
    sol = Solution()
    print(sol.zigzagLevelOrder(root))