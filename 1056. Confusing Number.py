class Solution:
    def confusingNumber(self, N: int) -> bool:
        """
        Idea:
            Two pointers.
            left and right pointer should be according to the rule
        """
        rules = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        n_str = str(N)
        left, right = 0, len(n_str) - 1
        diff = False
        while left <= right:
            if n_str[left] not in rules or n_str[right] not in rules:
                return False
            else:
                if rules[n_str[left]] != n_str[right] or rules[n_str[right]] != n_str[left]:
                    diff = True
                left += 1
                right -= 1
        return diff


