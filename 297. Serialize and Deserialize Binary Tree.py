from DS import TreeNode
import DS


class Codec:

    def serialize(self, root):
        """
        Uses preOrder to store information so that it can be done up to down in deserialize later
        """
        ans = []
        def preOrder(node):
            if node is not None:
                ans.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
            else:
                ans.append(None)
        preOrder(root)
        return " ".join(map(str, ans))

    def deserialize(self, data):
        """
        From https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)
        Uses iter to get the next node to process
        :param data:
        :return:
        """
        def build():
            n = next(dataIter)
            if n == 'None':
                return None
            else:
                node = TreeNode(int(n))
                node.left = build()
                node.right = build()
            return node
        dataIter = iter(data.split())
        return build()


if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,3,None,None,4,5])
    codec = Codec()
    s = codec.serialize(root)
    print(s)
    r = codec.deserialize(s)
    print(r)

