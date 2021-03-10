from DS import TreeNode
import DS
import collections


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """
        Idea:
            First, Do BFS, when reaches a node with depth d - 1, save its two node, create two new node, and connect
            the original nodes to the new nodes
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        que = collections.deque([(root, 1)])
        while que:
            curr, depth = que.pop()
            if depth == d - 1:
                left = curr.left
                right = curr.right
                curr.left = TreeNode(v)
                curr.right = TreeNode(v)
                curr.left.left = left
                curr.right.right = right
            else:
                if curr.left:
                    que.appendleft((curr.left, depth + 1))
                if curr.right:
                    que.appendleft((curr.right, depth + 1))
        return root


if __name__ == '__main__':
    sol = Solution()
    r = DS.arr2TreeNode([4, 2, None, 3, 1])
    r = sol.addOneRow(r, 1, 3)
    print(" ")
