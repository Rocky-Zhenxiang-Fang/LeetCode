from DS import *
from typing import List, Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self._dfs(root, [], targetSum)
        
        
    def _dfs(self, node: TreeNode, sums: List[int], targetSum: int) -> int:
        if not node:
            return 0
        res = 0
        if node.left:
            res += self._dfs(node.left, sums, targetSum)
        if node.right:
            res += self._dfs(node.right, sums,targetSum)
        for i in range(len(sums)):
            sums[i] += node.val
        sums.append(node.val)
        for s in sums:
            if s == targetSum:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    arr = [10,5,-3,3,2,None,11,3,-2,None,1]
    root = arr2TreeNode(arr)
    print(sol.pathSum(root, 8))