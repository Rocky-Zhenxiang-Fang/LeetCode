from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        This question is asking the max number of overlapping intervals
        We need a room for each start and clear up a room in each end
        Thus, we can sort each time and record if it is start or end
        if start, +1 room, if end -1 room
        return the max value between
        """
        import heapq
        times = []
        heapq.heapify(times)
        rooms = 0
        max_rooms = 0
        for i in intervals:
            heapq.heappush(times, (i[0], 1))
            heapq.heappush(times, (i[1], -1))
        while times:
            t = heapq.heappop(times)
            rooms += t[1]
            max_rooms = max(rooms, max_rooms)
        return max_rooms


if __name__ == '__main__':
    meetings = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.minMeetingRooms(meetings))
