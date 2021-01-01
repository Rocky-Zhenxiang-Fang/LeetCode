class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        found_odd = False
        s_counter = Counter(s)
        for k in s_counter:
            if s_counter[k] % 2 == 1:
                if found_odd:
                    return False
                else:
                    found_odd = True
        return True
