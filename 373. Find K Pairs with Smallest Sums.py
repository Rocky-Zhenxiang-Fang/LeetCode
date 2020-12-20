class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        pq = []
        res = []
        visited = {(0, 0)}
        heapq.heapify(pq)
        heapq.heappush(pq, (nums1[0] + nums2[0], (0, 0)))
        while len(res) < k and pq:
            ele = heapq.heappop(pq)[1]
            i, j = ele[0], ele[1]
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            if j + 1 < len(nums1) and (i, j + 1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
        return res


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 10
    sol = Solution()
    print(sol.kSmallestPairs(nums1, nums2, k))