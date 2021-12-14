from typing import List, Tuple

class Solution:
    def canTransforms(self, start: str, end: str) -> bool:
        start_data = [(ch, i) for i, ch in enumerate(start) if ch == "R" or ch == "L"]
        end_data = [(ch, i) for i, ch in enumerate(end) if ch == "R" or ch == "L"]

        if len(start_data) != len(end_data):
            return False

        for i in range(len(start_data)):
            start_LR, start_idx = start_data[i]
            end_LR, end_idx = end_data[i]
            if start_LR != end_LR or (start_LR == "R" and start_idx > end_idx) or (start_LR == "L" and start_idx < end_idx):
                return False

        return True

    def _extract_LR(original: str) -> List[Tuple[str, int]]:
        return [(ch, i) for i, ch in enumerate(original) if ch == "R" or ch == "L"]


if __name__ == '__main__':
    sol = Solution()
    tests = [("RXXLRXRXL", "XRLXXRRLX"), ("X", "L"), ("LLR", "RRL"), ("XL", "LX"), ("XLLR", "LXLX")]
    for t in tests:
        print(sol.canTransforms(t[0], t[1]))
