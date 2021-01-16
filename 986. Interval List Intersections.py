from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Idea:
            the overlap should be at the maximum of starts and the minimum of ends
            move the pointer for the one that ends earlier, if there is a tie, move any one
        """
        if not firstList or not secondList:
            return []
        ptr1, ptr2 = 0, 0
        res = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            sub = [max(firstList[ptr1][0], secondList[ptr2][0]), min(firstList[ptr1][1], secondList[ptr2][1])]
            if sub[1] >= sub[0]:
                res.append(sub)
            if firstList[ptr1][1] < secondList[ptr2][1]:
                ptr1 += 1
            else:
                ptr2 += 1
        return res



