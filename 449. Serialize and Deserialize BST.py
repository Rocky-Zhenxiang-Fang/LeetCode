from typing import List, Optional

from DS import TreeNode
import DS


class Codec:
    """
    Using post_order so that we will have children ready to point at
    We know that we can build Tree by having a inorder and (post or pre) traversal
    BST already has inorder, thus, we only need to store either one
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
            Idea:
                Do a post_order, store the result as string
        """
        res = []
        self._post_ser(root, res)
        return " ".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
            Idea:
                Right now we have a string with post_order
                We know that the end of data will be the root
                Also, to preserve BST, the next node can be a left leg only if the value is smaller then root value
                can be a right leg only if the value is bigger then the root value
        """
        data = data.split()
        return self._dec_helper(data, float("inf"), -float("inf"))

    def _post_ser(self, node: TreeNode, res: List[str]):
        if node:
            self._post_ser(node.left, res)
            self._post_ser(node.right, res)
            res.append(str(node.val))

    def _dec_helper(self, data: List[str], smaller, bigger) -> Optional[TreeNode]:
        if not data or int(data[-1]) > smaller or int(data[-1]) < bigger:
            return None
        else:
            root = TreeNode(int(data.pop()))
            root.right = self._dec_helper(data, smaller, root.val)  # reverse process, right goes first
            root.left = self._dec_helper(data, root.val, bigger)

            return root


if __name__ == '__main__':
    cod = Codec()
    dec = Codec()
    root = DS.arr2TreeNode([2, 1, 3])
    s = cod.serialize(root)
    print(s)
    r = dec.deserialize(s)
    print("done")
