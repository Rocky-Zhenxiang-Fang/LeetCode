from typing import List, Iterator


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        from collections import deque
        s_ptr = 0
        res = 0
        que = deque([(0, w) for w in words])
        while s_ptr < len(S):
            s_char = S[s_ptr]
            s_ptr, s_count = self.get_chunk(s_ptr, S)
            n = len(que)
            for _ in range(n):
                curr_ptr, curr_w = que.pop()
                curr_char = curr_w[curr_ptr]
                curr_ptr, curr_count = self.get_chunk(curr_ptr, curr_w)
                if s_count >= 3:
                    if curr_char == s_char and s_count >= curr_count:
                        if s_ptr >= len(S) and curr_ptr >= len(curr_w):
                            res += 1
                        elif s_ptr < len(S) and curr_ptr < len(curr_w):
                            que.appendleft((curr_ptr, curr_w))
                else:
                    if curr_char == s_char and s_count == curr_count:
                        if s_ptr >= len(S) and curr_ptr >= len(curr_w):
                            res += 1
                        elif s_ptr < len(S) and curr_ptr < len(curr_w):
                            que.appendleft((curr_ptr, curr_w))

        return res

    def get_chunk(self, ptr: int, w: str):
        count = 0
        head = w[ptr]
        while ptr < len(w):
            if w[ptr] == head:
                ptr += 1
                count += 1
            else:
                break
        return ptr, count


if __name__ == '__main__':
    sol = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(sol.expressiveWords(S, words))
