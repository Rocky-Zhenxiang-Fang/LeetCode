# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Use two pointers from headA and headB.
        if either of them reaches the end, the it will be redirect to other's head
        if both of them meet before it reaches the end again, the return the point that they meet
        Reason:
            Assume that two LinkedList have intersection, and the distance between their head and the
            intersection is A and B, and the distance from the intersection to the end is C.
            This algorithm makes both of the pointers travel A+B+C before they reach the intersection twice
        """
        aEnd = 0
        bEnd = 0
        aIte = headA
        bIte = headB

        while aEnd != 2 and bEnd != 2:
            if aIte == bIte:
                return aIte
            else:
                if not aIte.next:
                    aEnd += 1
                    aIte = headB
                else:
                    aIte = aIte.next

                if not bIte.next:
                    bEnd += 1
                    bIte = headA
                else:
                    bIte = bIte.next
        return None