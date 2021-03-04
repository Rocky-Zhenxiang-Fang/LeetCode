from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        Naive idea: For each s in S, find its right most item, this subarray should not be participate into two
        components
        Problem: There might be char inside this subarray that requires a longer subarray
        Solve: We need to check the right most item for each char in the subarray
        Pseudocode:
            find the right most index of each char and store it into a map
            initialize right, which stores the right index of this subarray
            for i in range(len(S)):
                check if the current element need more space:
                    if so, update right
                if i is at the right most index:
                    the subarray is verified, store its length
                    initialize right = -1
        """
        rights = {}
        res = []
        for i in range(len(S) - 1, -1, -1):
            if S[i] not in rights:
                rights[S[i]] = i
        left, right_most = 0, 0
        for i in range(len(S)):
            right_most = max(right_most, rights[S[i]])
            if i == right_most:
                res.append(right_most - left + 1)
                left = right_most + 1
        return res

if __name__ == '__main__':
    S = "caedbdedda"
    sol = Solution()
    print(sol.partitionLabels(S))

