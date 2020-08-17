from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, ne = len(gas) - 1, 0
        oil = gas[start] - cost[start]
        while start > ne:
            if oil >= 0:  # still have oil in the tank
                oil = oil + gas[ne] - cost[ne]
                ne += 1
            else:  # not having enough oil, start from the previous station
                start -= 1
                oil = oil + gas[start] - cost[start]

        if oil >= 0:
            return start
        else:
            return -1
