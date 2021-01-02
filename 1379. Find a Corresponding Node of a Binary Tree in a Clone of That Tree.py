from DS import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Idea, record how many steps needed for original to find target, repeat the steps on cloned and return the node
        """
        original_stack = [original]
        cloned_stack = [cloned]
        steps_needed = 0
        ori_iter = original
        cloned_iter = cloned
        while original_stack:
            ori_iter = original_stack.pop()
            if ori_iter == target:
                break
            else:
                steps_needed += 1
                if ori_iter.left:
                    original_stack.append(ori_iter.left)
                if ori_iter.right:
                    original_stack.append(ori_iter.right)
        while cloned_stack and steps_needed:
            cloned_iter = cloned_stack.pop()
            steps_needed -= 1
            if cloned_iter.left:
                cloned_stack.append(cloned_iter.left)
            if cloned_iter.right:
                cloned_stack.append(cloned_iter.right)

        return cloned_iter





