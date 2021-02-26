from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        curr, steps = 0, 0
        for i in range(n):
            answer[i] += steps
            curr += int(boxes[i])
            steps += curr
        curr, steps = 0, 0
        for i in range(n - 1, -1, -1):
            answer[i] += steps
            curr += int(boxes[i])
            steps += curr
        return answer

if __name__ == '__main__':
    sol = Solution()
    arr = "110"
    print(sol.minOperations(arr))