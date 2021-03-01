
# Definition for a Node.
from typing import List
import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []



class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        Idea:
            Flip the graph, do DFS from any node, return the end
            Keep a parent map, stores {node: parent}
            Use this map, continue iterating until a node does not have any parent, this is the answer
        """
        parent = {}
        for t in tree:
            for nei in t.children:
                parent[nei] = parent.get(nei, []) + [t]
        root = tree[0]
        while root in parent:
            root = parent[root]

        return root


