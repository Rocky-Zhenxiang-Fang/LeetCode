from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        This number is asking maximum number of overlapping rooms
        When a meeting starts, we need one room, when one ends, we can release one room
        We can keep a track of how many rooms are used by +1 at start and -1 at end
        Sort each time regarding which meeting does it belongs to
        """
        heap = []
        max_room = 0
        curr_room = 0
        heapq.heapify(heap)
        for i in intervals:
            heapq.heappush(heap, (i[0], "start"))
            heapq.heappush(heap, (i[1], "end"))
        while heap:
            t, condition = heapq.heappop(heap)
            if condition == "start":
                curr_room += 1
                max_room = max(max_room, curr_room)
            else:
                curr_room -= 1
        return max_room


if __name__ == '__main__':
    meetings = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.minMeetingRooms(meetings))
