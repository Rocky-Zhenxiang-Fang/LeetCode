from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        erased_elements = set()
        left, right = 0, 0
        res = 0
        temp_res = 0
        while right < len(nums):
            while nums[right] in erased_elements:
                erased_elements.remove(nums[left])
                temp_res -= nums[left]
                left += 1
            
            erased_elements.add(nums[right])
            temp_res += nums[right]
            right += 1
            res = max(res, temp_res)
        return res


if __name__ == "__main__":
    sol = Solution()
    tests = (
        ([4,2,4,5,6], 17),
        ([5,2,1,2,5,2,1,2,5], 8),
        ([10000,1,10000,1,1,1,1,1,1], 10001),
        )
    for test_input, expected_result in tests:
        if res := sol.maximumUniqueSubarray(test_input) != expected_result:
            print(f"[ERROR] Test input {test_input} failed, expected = {expected_result}, returned: {res}")
        else:
            print(f"[INFO] Test input {test_input} passed")

