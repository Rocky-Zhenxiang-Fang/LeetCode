class ImmutableListNode:
    def printValue(self) -> None:  # print the value of this node.
        pass

    def getNext(self) -> 'ImmutableListNode':  # return the next node
        pass


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        store = []
        while head:
            store.append(head)
            head = head.getNext()
        while store:
            curr = store.pop()
            curr.printValue()
