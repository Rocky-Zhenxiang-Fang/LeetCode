import DS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees_bad(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Idea, BFS, add node value if both value exist, if not, link the existing node
        To prevent null node, if a node cannot be added, create a dummy node as a place holder
        Super bad implemented
        """
        from collections import deque
        if not t1 and t2:
            return t2
        elif not t2 and t1:
            return t1
        elif not t1 and not t2:
            return None
        t1_que = deque([t1])
        t2_que = deque([t2])
        head = TreeNode(t1.val + t2.val)
        head_que = deque([head])
        while t1_que or t2_que:
            t1_ptr = t1_que.pop()
            t2_ptr = t2_que.pop()
            ptr = head_que.pop()
            if t1_ptr.left and t2_ptr.left:
                ptr.left = TreeNode(t1_ptr.left.val + t2_ptr.left.val)
                t1_que.appendleft(t1_ptr.left)
                t2_que.appendleft(t2_ptr.left)
                head_que.appendleft(ptr.left)
            elif t1_ptr.left:
                ptr.left = t1_ptr.left
                t1_que.appendleft(t1_ptr.left)
                t2_que.appendleft(TreeNode(0))
                head_que.appendleft(ptr.left)
            elif t2_ptr.left:
                ptr.left = t2_ptr.left
                t1_que.appendleft(TreeNode(0))
                t2_que.appendleft(t2_ptr.left)
                head_que.appendleft(ptr.left)
            if t1_ptr.right and t2_ptr.right:
                ptr.right = TreeNode(t1_ptr.right.val + t2_ptr.right.val)
                t1_que.appendleft(t1_ptr.right)
                t2_que.appendleft(t2_ptr.right)
                head_que.appendleft(ptr.right)
            elif t1_ptr.right:
                ptr.right = t1_ptr.right
                t1_que.appendleft(t1_ptr.right)
                t2_que.appendleft(TreeNode(0))
                head_que.appendleft(ptr.right)
            elif t2_ptr.right:
                ptr.right = t2_ptr.right
                t1_que.appendleft(TreeNode(0))
                t2_que.appendleft(t2_ptr.right)
                head_que.appendleft(ptr.right)
        return head

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Idea: merge t2 into t1, recursive, deal with this node first, then deal with its children
        """
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1



if __name__ == '__main__':
    sol = Solution()
    head_1 = DS.arr2TreeNode([1, 3, 2, 5])
    head_2 = DS.arr2TreeNode([2, 1, 3, None, 4, None, 7])
    head_3 = sol.mergeTrees(head_1, head_2)
    print(head_3)

