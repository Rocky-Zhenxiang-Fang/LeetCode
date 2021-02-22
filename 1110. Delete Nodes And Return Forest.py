from typing import List, Optional

from DS import TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        Idea:
            If a node has no parent and do not need to be deleted, this is a answer
            Use preorder to assign left and right node
        """
        res = []
        to_delete = set(to_delete)

        def pre_order(node: TreeNode, has_parent: bool) -> Optional[TreeNode]:
            if node:
                delete = False
                if node.val in to_delete:  # check if this node should be delete
                    delete = True
                if not has_parent and not delete:
                    res.append(node)
                node.left = pre_order(node.left, not delete)
                node.right = pre_order(node.right, not delete)
                return node if not delete else None  # if deleted, the parent should not have this node

        pre_order(root, False)
        return res
