from DS import TreeNode


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        val1 = set()
        stack = [root1]
        while stack:
            node = stack.pop()
            val1.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        stack = [root2]
        while stack:
            node = stack.pop()
            if target - node.val in val1:
                return True
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return False


