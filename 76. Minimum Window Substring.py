import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Idea:
            This problem can be separate into two parts
            1. To get the range of a subarray, this will be done using two pointers
            2. To check if the subarray fulfills the requirements, this will be done using counter and set
        Alg:
            Use two pointer to get the size of the subarray
            While the subarray does not have enough chars, increase right
            While the subarray does have enough chars, remove left
            At here, s[left - 1: right + 1] will have the chars to form t, compare its length with res

            To check if subarray have enough number, we make two counter and a set.
                t_counter: stores the number of each char needed
                s_counter: stores the number of each char is in the subarray
                satisfied: stores the chars that fulfills s_counter[ch] >= t_counter[ch]
                In the expanding stage, if s_counter[ch] == t_counter[ch], satisfied.add(ch)
                when len(satisfied) == len(t_counter), stop expanding
                In the shrinking stage, if s_counter[ch] < t_counter[ch], satisfied.remove(ch)
                when len(satisfied) != len(t_counter), stop shrinking
        """
        res = ""
        left, right = 0, 0
        t_counter = collections.Counter(t)
        s_counter = {ch: 0 for ch in t_counter}
        satisfied = set()
        while right < len(s):
            while len(satisfied) != len(t_counter) and right < len(s):
                if s[right] in s_counter:
                    s_counter[s[right]] += 1
                    if s_counter[s[right]] == t_counter[s[right]]:
                        satisfied.add(s[right])
                right += 1
            if len(satisfied) == len(t_counter):
                while len(satisfied) == len(t_counter):
                    if s[left] in s_counter:
                        s_counter[s[left]] -= 1
                        if s_counter[s[left]] < t_counter[s[left]]:
                            satisfied.remove(s[left])
                    left += 1

                if not res or len(res) > right - left + 1:
                    res = s[left - 1: right]
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "ab"
    t = "a"
    print(sol.minWindow(s, t))
