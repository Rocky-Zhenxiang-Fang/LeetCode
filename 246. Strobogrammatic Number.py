class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        check = {
            "1": "1",
            "0": "0",
            "8": "8",
            "6": "9",
            "9": "6"
        }
        left, right = 0, len(num) - 1
        while left < right:
            if num[left] not in check or num[right] not in check:
                return False
            elif check[num[left]] != num[right]:
                return False
            else:
                left += 1
                right -= 1
        if left == right:
            if num[left] not in {"1", "0", "8"} or num[right] not in {"1", "0", "8"}:
                return False
        return True


if __name__ == '__main__':
    num = "69"
    sol = Solution()
    print(sol.isStrobogrammatic(num))