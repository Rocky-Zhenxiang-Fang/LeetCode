# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arr2TreeNode(arr) -> TreeNode:
    nodeArr = [TreeNode]
    for n in arr:
        if n is not None:
            nodeArr.append(TreeNode(n))
        else:
            nodeArr.append(None)
    for i in range(1, len(nodeArr)):
        if nodeArr[i]:
            if 2 * i < len(nodeArr):
                nodeArr[i].left = nodeArr[2 * i]
            if 2 * i + 1 < len(nodeArr):
                nodeArr[i].right = nodeArr[2 * i + 1]
    return nodeArr[1]
