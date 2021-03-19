class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []     # this stores all values into it
        self.min_stack = []     # this stores values that is smaller then current smallest value


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]