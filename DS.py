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


class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def arr2LinkedNode(arr) -> ListNode:
    prev = None
    for i in range(len(arr) - 1, -1, -1):
        current_node = ListNode(arr[i])
        current_node.next = prev
        prev = current_node
    return prev


def print_ListNode(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


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
