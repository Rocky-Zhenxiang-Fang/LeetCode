from typing import List


class Solution:
    def searchSlow(self, nums: List[int], target: int) -> int:
        """
        1. Find the pivot of nums
        2. Do binary search on nums[:pivot], if founded, return its index
        3. Do binary search on nums[pivot:], if founded, return its index (pivot is added in start)
        4. if cannot return, return -1
        5. Time Complex O(n) (finding the pivot)
        """
        if not nums:
            return -1
        pivot = nums.index(min(nums))

        def binSearch(start, end):
            if start > end:
                return - 1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binSearch(start, mid - 1)
            else:
                return binSearch(mid + 1, end)

        firstHalf = binSearch(0, pivot - 1)
        if firstHalf != -1:
            return firstHalf
        secHalf = binSearch(pivot, len(nums) - 1)
        if secHalf != -1:
            return secHalf
        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        Instead of doing two binary searches, we take advantage of a pivoted sorted list have at least a side sorted.
        If our target lays in the sorted range, we do a BS in that range, else, do at another range
        Also, we needed to check if its left pivot or right pivot in every iteration to decide where is the sorted list
        1. start, end = 0, len(nums) - 1
        2. iterate it until start > end:
            2.1 if nums[mid] == target: return mid
            2.2 if not, find the sorted side
            2.3 if target is at that side, search that side, else, sort the other
        3. return -1
        """
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:  # means that the left side is sorted.
                # Equal is there to prevent if start == mid
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # means that the right side is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1]
    target = 1
    print(sol.search(nums, target))
