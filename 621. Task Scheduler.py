from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        We want to separate the same task in n spaces between
        The time will be dominate by the most frequently shown element
        """
        from collections import Counter
        tasksCounter = list(Counter(tasks).values())
        maxOccur = max(tasksCounter)
        numOfMax = tasksCounter.count(maxOccur)
        return max(len(tasks), (maxOccur - 1) * (n + 1) + numOfMax)


if __name__ == '__main__':
    sol = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(sol.leastInterval(tasks, n))




