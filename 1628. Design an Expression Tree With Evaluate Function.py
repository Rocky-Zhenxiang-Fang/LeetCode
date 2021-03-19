import abc
from abc import ABC, abstractmethod
from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    # define your fields here
    def __init__(self, val: str, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right

    # @abstractmethod
    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        else:
            left = self.left.evaluate()
            right = self.right.evaluate()
            if self.val == "+":
                return left + right
            elif self.val == "-":
                return left - right
            elif self.val == "*":
                return left * right
            else:
                return int(left / right)


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        left_first = True
        for p in postfix:
            if p.isdigit():
                stack.append(Node(p))
            else:
                first = stack.pop()
                second = stack.pop()
                stack.append(Node(p, second, first))
                left_first = not left_first
        return stack[0]


if __name__ == '__main__':
    s = ["3", "4", "+", "2", "*", "7", "/"]
    tb = TreeBuilder()
    n = tb.buildTree(s)
    print(n.evaluate())

"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
