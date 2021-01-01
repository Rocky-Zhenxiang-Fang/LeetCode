from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Idea: for each person, find the "penalty" for mis sending the person
            the much the penalty, distribute the person first
        """
        import heapq
        pq = []
        heapq.heapify(pq)
        first_city = len(costs) // 2
        second_city = len(costs) // 2
        res = 0
        for c in costs:
            a = [min(c) - max(c)] + c
            heapq.heappush(pq, a)
        while pq:
            person = heapq.heappop(pq)
            if person[2] > person[1]:
                if first_city > 0:
                    first_city -= 1
                    res += person[1]
                else:
                    second_city -= 1
                    res += person[2]
            else:
                if second_city > 0:
                    second_city -= 1
                    res += person[2]
                else:
                    first_city -= 1
                    res += person[1]
        return res


if __name__ == '__main__':
    sol = Solution()
    costs = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
    print(sol.twoCitySchedCost(costs))
