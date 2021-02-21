from typing import List
import DS

from DS import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        Idea:
            For each unique tree, assign it a unique id which is equal to the number of unique registered at that time
            By using a post order, the subtree can be represented as (val, left_id, right_id)
            Use two dicts, one to store id of each subtree, one for storing nodes that have the same id
        """
        from collections import defaultdict
        tree_ids = defaultdict()
        id_node = defaultdict(list)
        tree_ids.default_factory = tree_ids.__len__

        def post_order(node: TreeNode) -> int:
            if node:
                node_id = tree_ids[(node.val, post_order(node.left), post_order(node.right))]
                id_node[node_id].append(node)
                return node_id
            return -1

        post_order(root)
        return [id_node[k][0] for k in id_node if len(id_node[k]) > 1]


if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2TreeNode([2, 1, 1])
    r = sol.findDuplicateSubtrees(root)
    print(r)
