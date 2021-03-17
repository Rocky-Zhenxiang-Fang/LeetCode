# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []  # List[Node]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Idea:
            Do DFS
            Maintain a copied map that matches the original node to the copied node
            Also maintain a visited to prevent looking back
        """
        if not node:
            return node
        stack = [node]
        copied = {node: Node(node.val)}
        while stack:
            curr = stack.pop()
            for child in curr.neighbors:
                if child not in copied:
                    copied[child] = Node(child.val)
                    stack.append(child)
                copied[curr].neighbors.append(copied[child])
        return copied[node]



