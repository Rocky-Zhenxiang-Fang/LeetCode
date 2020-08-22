from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for item in nums:
            if item in visited:
                return True
            else:
                visited.add(item)
        return False


if __name__ == '__main__':
    arr = [1,1,1,3,3,4,3,2,4,2]
    sol = Solution()
    print(sol.containsDuplicate(arr))