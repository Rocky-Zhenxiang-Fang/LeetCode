from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Idea:
            Compare each word to the one right to them, if that the right one is bigger,then return false
        """
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i

        for j in range(len(words) - 1):  # not comparing the right most one
            right_word = words[j + 1]
            left_word = words[j]
            if len(right_word) < len(left_word) and left_word[:len(right_word)] == right_word:
                return False
            for k in range(min(len(right_word), len(left_word))):
                if order_map[left_word[k]] < order_map[right_word[k]]:
                    break
                elif order_map[left_word[k]] > order_map[right_word[k]]:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    test1_arr = ["hello","leetcode"]
    test1_order = "hlabcdefgijkmnopqrstuvwxyz"
    test2_arr = ["word","world","row"]
    test2_order = "worldabcefghijkmnpqstuvxyz"
    test3_arr = ["apple","app"]
    test3_order = "abcdefghijklmnopqrstuvwxyz"
    print(sol.isAlienSorted(test1_arr, test1_order))
    print(sol.isAlienSorted(test2_arr, test2_order))
    print(sol.isAlienSorted(test3_arr, test3_order))