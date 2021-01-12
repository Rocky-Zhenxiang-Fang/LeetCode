from DS import TreeNode


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        Idea:
            Do a inorder traversal, keep only the previous val
            In one call, if node.val == target: return target
            Else if node.val > target > previous: return the closer one
            Else: record this val, keep goining
            At the end, if cannot find this condition, meanning that target is bigger then any other element, return the biggest
        """
        self.prev = -float("inf")
        self.ans = 0
        def inorder(node):
            if node.left:
                inorder(node.left)
            if node.val >= target > self.prev:
                self.ans = min(abs(self.prev - target), abs(node.val - target))
            else:
                self.prev = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.prev if target >= self.prev else self.ans


