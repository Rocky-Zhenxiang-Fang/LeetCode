from DS import TreeNode


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        """
        String is stored in order of preorder traversal with the left leg always presented
        When see "(", add node to stack
        When see ")", pop node
        """
        curr_num = float("inf")
        stack = []
        sign = "+"
        for ch in s:
            if ch == "-":
                sign = "-"
            elif ch.isdigit():
                curr_num = int(ch) if curr_num == float("inf") else curr_num * 10 + int(ch)
            else:
                if curr_num != float("inf"):
                    curr_node = TreeNode(curr_num) if sign == "+" else TreeNode(-curr_num)
                    curr_num = float("inf")
                    sign = "+"
                    if stack:
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = curr_node
                        else:
                            parent.right = curr_node
                    stack.append(curr_node)
                if ch == ")":
                    stack.pop()
        if stack:
            return stack[0]
        elif len(s) == 0:
            return None
        else:
            return TreeNode(curr_num) if sign == "+" else TreeNode(-curr_num)

