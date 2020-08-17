from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        q = deque()  # stores the children
        nq = deque()  # stores the next q
        res = []  # stores the answer

        if not root:
            return [[]]
        q.appendleft(root)

        while True:
            subRes = []
            while len(q) != 0:
                r: 'Node' = q.pop()
                subRes.append(r.val)
                for c in r.children:
                    nq.appendleft(c)
            res.append(subRes)

            if len(nq) == 0:
                return res
            q = nq.copy()
            nq.clear()
