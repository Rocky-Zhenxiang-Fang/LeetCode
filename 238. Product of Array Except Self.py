from typing import List


class Solution:
    def productExceptSelf(self, nums):
        """
        Idea: for each n, the answer is the product of all element from the left and all element from the right
            thus, we can first go from the left to the right, this gives us the product of all elements from the left
            then, do it again from the right, this gives us the product of all elements from the right
            finally, multiply them together
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.productExceptSelf(arr))
