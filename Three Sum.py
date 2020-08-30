class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        for i in range(len(nums) - 1):
            tar = 0 - nums[i]
            sub = self.twoSum(nums[i + 1:], tar)
            if len(sub) == 0:
                continue
            ans.add(([nums[i]] + sub).sort())
        return list(ans)

    def twoSum(self, nums, target):
        visited = set()
        for n in nums:
            if target - n in visited:
                return [target - n, n]
            else:
                visited.add(n)
        return []


if __name__ == '__main__':
    arr = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(arr))