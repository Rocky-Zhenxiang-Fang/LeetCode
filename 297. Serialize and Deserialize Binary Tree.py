from typing import List, Optional

from DS import TreeNode
import DS


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
            Do post order so that we can dump used node rather then keeping a pointer
        """
        res = []
        self._ser(root, res)
        return " ".join(res)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
            Since it is stored in post_order, we can make each node from behind, only continue if the current node is not None
            Remember to go right first since it is a reverse process
        """
        data = data.split()
        return self._des(data)

    def _ser(self, node: TreeNode, res: List[str]):
        if not node:
            res.append("None")
        else:
            self._ser(node.left, res)
            self._ser(node.right, res)
            res.append(str(node.val))

    def _des(self, data: List[str]) -> Optional[TreeNode]:
        val = data.pop()
        if val == "None":
            return None
        else:
            root = TreeNode(int(val))
            root.right = self._des(data)
            root.left = self._des(data)
            return root


if __name__ == '__main__':
    root = DS.arr2TreeNode([1, 2, 3, None, None, 4, 5])
    codec = Codec()
    s = codec.serialize(root)
    print(s)
    r = codec.deserialize(s)
    print(r)
