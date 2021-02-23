from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        Idea:
            For each row, it must start with a string, and rows starts with the same string will end at the same string
            and finish the same number of line.
        Alg:
            For each row, check its start,
                If not visited before, add each string one by one.
                During the process, check if it reaches the end
                Let the pointer point at the next string
        """
        seen = {}   # string_id:　(number of lines, next_string_id)
        s_id = 0
        res = 0
        for r in range(rows):
            if s_id not in seen:
                c = 0
                end_count = 0
                start_id = s_id
                while c + len(sentence[s_id]) <= cols:
                    c += len(sentence[s_id]) + 1
                    if s_id != len(sentence) - 1:
                        s_id += 1
                    else:
                        end_count += 1
                        s_id = 0
                seen[start_id] = (end_count, s_id)
                res += end_count
            else:
                res += seen[s_id][0]
                s_id = seen[s_id][1]

        return res


if __name__ == '__main__':
    rows = 4
    cols = 5
    sentence = ["I", "had", "apple", "pie"]
    sol = Solution()
    print(sol.wordsTyping(sentence, rows, cols))


