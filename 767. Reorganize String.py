class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        Idea:
            Greedy:
                In each iteration, put two the most frequently shown char into result
        """
        from collections import Counter
        import heapq
        res = []
        s_counter = Counter(S)
        pq = []
        heapq.heapify(pq)   # (frequency, char)
        for k in s_counter:
            heapq.heappush(pq, (-s_counter[k], k))
        if -pq[0][0] > (len(S) + 1) // 2:
            return ""

        while pq:
            if len(pq) > 1:
                first = heapq.heappop(pq)
                second = heapq.heappop(pq)
                res.append(first[1])
                res.append(second[1])
                if first[0] + 1 < 0: heapq.heappush(pq, (first[0] + 1, first[1]))
                if second[0] + 1 < 0: heapq.heappush(pq, (second[0] + 1, second[1]))
            else:
                res.append(pq[0][1])
                break
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganizeString("aab"))
