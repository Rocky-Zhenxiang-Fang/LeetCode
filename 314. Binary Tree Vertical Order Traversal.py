import collections
from typing import List

from DS import TreeNode


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        x_map = {}  # col: [values]
        que = collections.deque([(root, 0)])  # node: col
        while que:
            curr, col = que.pop()
            x_map[col] = x_map.get(col, []) + [curr.val]
            if curr.left:
                que.appendleft((curr.left, col - 1))
            if curr.right:
                que.appendleft((curr.right, col + 1))
        res = sorted([(k, v) for k, v in x_map.items()], key=lambda x: x[0])
        return [x[1] for x in res]
