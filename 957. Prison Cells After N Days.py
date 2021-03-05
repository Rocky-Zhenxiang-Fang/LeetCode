from typing import List, Tuple


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        Idea: Since we know that there are only eight cells, their only be 2^8 different combinations, and the rule
            only takes the current cells as input, making it possible to loop.
            Thus, we can memorize the paths, if we encounter a visited situation, we can fast forward
        """
        seen = dict()
        is_fast_forwarded = False

        while N > 0:
            # we only need to run the fast-forward once at most
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N
                    N %= seen[state_key] - N
                    is_fast_forwarded = True
                else:
                    seen[state_key] = N

            # check if there is still some steps remained,
            # with or without the fast-forwarding.
            if N > 0:
                N -= 1
                next_day_cells = self.next_day(cells)
                cells = next_day_cells

        return cells


    def next_day(self, cells: List[int]) -> List[int]:
        res = [0]
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                res.append(1)
            else:
                res.append(0)
        return res + [0]



if __name__ == '__main__':
    cells = [1,0,0,1,0,0,1,0]
    N = 1000000000
    cells_2 = [0, 1, 0, 1, 1, 0, 0, 1]
    N_2 = 7
    sol = Solution()
    print(sol.prisonAfterNDays(cells, N))
