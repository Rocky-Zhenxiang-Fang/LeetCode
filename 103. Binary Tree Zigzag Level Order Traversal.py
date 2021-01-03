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
        Idea:
            Do a normal level order traversal, however, before adding it to the res, reverse it if necessary
        """
        from collections import deque

        res = []
        que = deque([root])
        left = True
        if root:
            while que:
                n = len(que)
                sub = []
                for _ in range(n):
                    node = que.pop()
                    sub.append(node.val)
                    if node.left:
                        que.appendleft(node.left)
                    if node.right:
                        que.appendleft(node.right)
                if left:
                    res.append(sub)
                else:
                    res.append(sub[::-1])
                left = not left
        return res


if __name__ == '__main__':
    root = DS.arr2TreeNode([3, 9, 20, None, None, 15, 7])
    sol = Solution()
    print(sol.zigzagLevelOrder(root))
