from typing import List
import collections
from DS import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return [0]
        res = []
        que = collections.deque([root])
        while que:
            next_que = collections.deque()
            acc, num = 0, 0
            while que:
                curr = que.pop()
                acc += curr.val
                num += 1
                if curr.left:
                    next_que.append(curr.left)
                if curr.right:
                    next_que.append(curr.right)
            res.append(acc / num)
            que = next_que
        return res

