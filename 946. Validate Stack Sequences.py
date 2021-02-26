from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Idea:
            Direct approach:
                push elements in pushed into a stack in order
                    if at any time, the value is the same as the first element in popped, pop it
                check if the stack is empty after
        """
        stack = []
        id = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[id]:
                stack.pop()
                id += 1
        return len(stack) == 0
