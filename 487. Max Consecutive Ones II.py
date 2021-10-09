from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Idea: 
        # Since zero can be fliped to one, the minimum res is 1
        # Starting from the start of the arr, if we meet a zero, we close the current ones, try to connect it to the one before, and flip is one to 1
        return 0


if __name__ == '__main__':
    sol = Solution()
    arr = [1,0,1,1,0]
    print(sol.findMaxConsecutiveOnes(arr))