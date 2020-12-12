from typing import Set

from DS import TreeNode
from DS import arr2TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        Do post order two times, one for finding the deepest node and the other one to find the lowest common
        ancestor of them
        My solution: very long implemented
        """
        common_ancestor = None
        level_map = [-1, set()]

        def post_order_first(level: int, node: TreeNode) -> None:
            if node is None:
                return
            if level > level_map[0]:
                level_map[0] = level
                level_map[1] = {node}
            elif level == level_map[0]:
                level_map[1].add(node)
            post_order_first(level + 1, node.left)
            post_order_first(level + 1, node.right)

        def post_order_second(node: TreeNode) -> (TreeNode, Set[TreeNode]):
            result_1 = (None, set())
            result_2 = (None, set())
            if node.left:
                result_1 = post_order_second(node.left)
                if result_1[0] is not None:
                    return result_1
            if node.right:
                result_2 = post_order_second(node.right)
                if result_2[0] is not None:
                    return result_2
            seen = result_1[1].union(result_2[1])
            if node in level_map[1]:
                seen.add(node)
            if len(seen) == len(level_map[1]):
                return node, seen
            else:
                return None, seen

        post_order_first(0, root)
        common_ancestor = post_order_second(root)[0]
        return common_ancestor

    def subtreeWithAllDeepest_2(self, root):
        """
        Better implemented version using the same idea
        """
        # Tag each node with it's depth.
        depth = {None: -1}

        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        max_depth = max(depth.itervalues())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)

    def subtreeWithAllDeepest_3(self, root):
        """
        One pass solution, iterating using post order
        In each recursion call, returns the maximum depth and a node
        """

        def deep(root):
            """
            Recursion post_order_traversal
            returns the maximum depth and a node
            the maximum depth is determined by the maximum depth of its subtrees
            if the maximum depth of both subtrees are the same,
                this means that the current node is the lowest common ancestor of the max depth tree so far
            if they are not the same:
                return the answer that have the max depth tree
            """
            if not root: return 0, None
            l, r = deep(root.left), deep(root.right)
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            elif l[0] < r[0]:
                return r[0] + 1, r[1]
            else:
                return l[0] + 1, root

        return deep(root)[1]


if __name__ == '__main__':
    sol = Solution()
    arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    test_tree = arr2TreeNode(arr)
    ans = sol.subtreeWithAllDeepest(test_tree)
    print(ans.val)
