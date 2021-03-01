from typing import List, Optional

from DS import TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        Idea:
            After delete, a node will be a root if and only if it does not have a parent and itself haven't be deleted
            Also, if it self is deleted, it should let it parent know so that the parent can remove that leg
        Alg:
            Do DFS, pass in node, does it have a parent
        """
        res = []
        to_delete = set(to_delete)

        def dfs(node: TreeNode, parent: bool) -> Optional[TreeNode]:
            if node:
                delete = node.val in to_delete
                if not parent and not delete:
                    res.append(node)
                node.left = dfs(node.left, not delete)
                node.right = dfs(node.right, not delete)
                return node if not delete else None
        dfs(root, False)
        return res
