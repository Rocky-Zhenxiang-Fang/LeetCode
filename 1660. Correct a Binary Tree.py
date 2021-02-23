from DS import TreeNode


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        from collections import deque
        que = deque([(root, None, None)])  # puts (node, parent, left or right)
        seen = set()
        while que:
            n = len(que)
            for _ in range(n):
                curr, parent, side = que.pop()
                if curr.right:
                    if curr.right in seen:
                        if side == "left":
                            parent.left = None
                        else:
                            parent.right = None
                            break
                    else:
                        seen.add(curr.right)
                        que.appendleft((curr.right, curr, "right"))
                if curr.left:
                    que.appendleft((curr.left, curr, "left"))
                    seen.add(curr.left)

        return root
