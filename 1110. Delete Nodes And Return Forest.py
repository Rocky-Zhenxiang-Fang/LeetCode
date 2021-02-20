from typing import List, Optional

from DS import TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        Idea:
            If a root has no parent and itself does not be deleted, add it to ans
        """
        res = []
        to_delete = set(to_delete)

        def helper(node: TreeNode, has_parent: bool) -> Optional[TreeNode]:
            if not node:
                return None
            delete = True if node.val in to_delete else False
            if not has_parent and not delete:
                res.append(node)
            node.left = helper(node.left, not delete)
            node.right = helper(node.right, not delete)
            return node if not delete else None

        helper(root, False)
        return res
