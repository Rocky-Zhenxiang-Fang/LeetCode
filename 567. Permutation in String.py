import collections
class Solution:
    def _update_counter(self, counter, string, right, left) -> bool:
        """
        Returns true if the counter is empty after updating 
        """
        if left >= 0:
            counter[string[left]] += 1
        if counter[string[left]] == 0:
            del counter[string[left]]
        counter[string[right]] -= 1
        if counter[string[right]] == 0:
            del counter[string[right]]
        return not counter
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = collections.Counter(s1)
        for right in range(len(s2)):
            if self._update_counter(s1_counter, s2, right, right - len(s1)):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    tests = [["ab", "eidbaooo"], 
            ["ab","eidboaoo"]]
    for t in tests:
        print(sol.checkInclusion(t[0], t[1]))
