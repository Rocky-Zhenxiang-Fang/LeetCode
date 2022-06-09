from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        old_rows, old_cols = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(old_rows)] for _ in range(old_cols)]
        for old_row_idx, old_row in enumerate(matrix):
            for old_col_idx, element in enumerate(old_row):
                new_matrix[old_col_idx][old_row_idx] = element
        return new_matrix


if __name__ == "__main__":
    sol = Solution()
    test_1 = ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]])
    test_2 = ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]])
    tests = (test_1, test_2)
    for idx, (test_case, expected_result) in enumerate(tests):
        result = sol.transpose(test_case)
        print(result)
        if result == expected_result:
            print(f"test {idx + 1} passed")
        else:
            print(f"test {idx + 1} failed")
