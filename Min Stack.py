class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        return self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.minStack[0]

    def getMin(self):
        """
        :rtype: int
        """
        res = min(self.minStack)
        self.minStack.remove(res)
        return res


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
