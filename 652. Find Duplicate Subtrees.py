import collections
from typing import List
import DS

from DS import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root):
        def getid(root):
            if root:
                id = treeid[root.val, getid(root.left), getid(root.right)]
                trees[id].append(root)
                return id

        trees = collections.defaultdict(list)
        treeid = collections.defaultdict()
        treeid.default_factory = treeid.__len__
        getid(root)
        return [roots[0] for roots in trees.values() if roots[1:]]


if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2TreeNode([2, 1, 1])
    r = sol.findDuplicateSubtrees(root)
    print(r)
