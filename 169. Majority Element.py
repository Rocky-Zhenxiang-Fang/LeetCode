from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm
        Treat each num as a candidate
        If I found that someone vote against him, reduce his vote,
        If his vote is reduced to zero, means that he is no longer a candidate, then the next one is candidate
        If the candidate survived to the last, then it is teh majority
        """
        cnt = 0
        candidate = 0
        for n in nums:
            if cnt == 0:
                candidate = n
            cnt += (1 if candidate == n else -1)
        return candidate


if __name__ == '__main__':
    arr = [3,2,3]
    sol = Solution()
    print(sol.majorityElement(arr))
