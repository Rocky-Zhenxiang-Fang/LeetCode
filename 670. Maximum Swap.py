class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Idea:
            1. We want to put the first k number as sorted order (Not a good example)
            2. If two same number, swap the later one
            3. Going from right to left, do two judgements
                1. check if this number is bigger then nums[temp_right], if so, meaning that this number should be swap ahead
                2. check if this number is smaller then nums[temp_right], if so, meaning that this number should be swap
                behind.
            # additional temp_right is used to prevent update right before finding a pair
        """
        nums = [int(n) for n in str(num)]
        left, right, temp_right = 0, 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[temp_right]:
                temp_right = i
            elif nums[i] < nums[temp_right]:
                left, right = i, temp_right
        nums[left], nums[right] = nums[right], nums[left]
        return int("".join([str(n) for n in nums]))


if __name__ == '__main__':
    sol = Solution()
    test1 = 98368
    test2 = 9973
    test3 = 2736
    print(sol.maximumSwap(test1))
    print(sol.maximumSwap(test2))
    print(sol.maximumSwap(test3))
