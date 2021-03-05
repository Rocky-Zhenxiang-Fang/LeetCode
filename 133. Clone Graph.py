# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []  # List[Node]


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Idea:
            Do a DFS:
                For each neighbors:
                    if neighbor node have not be created:
                        create the node
                    link node and neighbor together
        """
        copy_map = {node: Node(node.val)}
        visited = set()
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for nei in curr.neighbors:
                    if nei not in copy_map:
                        copy_map[nei] = Node(nei.val)
                    copy_map[nei].neighbors.append(copy_map[curr])
                    copy_map[curr].neighbors.append(copy_map[nei])
        return copy_map[node]




