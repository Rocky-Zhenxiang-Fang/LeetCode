class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        max_id = len(nums) - 1
        left, right = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[max_id]:
                max_id = i  # found someone bigger then the current pair
            elif nums[i] < nums[max_id]:
                left, right = i, max_id  # found a pair that is swappable
        # since its going from right to left, left will getting smaller, and the result number will be bigger
        nums[left], nums[right] = nums[right], nums[left]
        return int("".join([str(x) for x in nums]))


if __name__ == '__main__':
    sol = Solution()
    test1 = 98368
    test2 = 9973
    test3 = 2736
    print(sol.maximumSwap(test1))
    print(sol.maximumSwap(test2))
    print(sol.maximumSwap(test3))
