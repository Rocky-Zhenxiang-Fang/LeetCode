from typing import List, Tuple


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        After a series of instructions, if the robot returns to the start, it will form a cycle
        We can run four iterations and see if any time it returns to the origin
        """
        end = [0, 0]
        face = (0, 1)
        for i in range(4):
            end, face = self.run(end, face, instructions)
            if end == [0, 0]:
                return True
        return False

    def run(self, start: List[int], face: Tuple[int], instructions: str):
        # face = (0, 1) -> north, face = (-1, 0) -> west, face = (0, -1) -> south, face = (1, 0) -> east
        for ch in instructions:
            if ch == "G":
                start[0] += face[0]
                start[1] += face[1]
            elif ch == "L":
                if face == (0, 1):
                    face = (-1, 0)
                elif face == (-1, 0):
                    face = (0, -1)
                elif face == (0, -1):
                    face = (1, 0)
                else:
                    face = (0, 1)
            else:
                if face == (0, 1):
                    face = (1, 0)
                elif face == (1, 0):
                    face = (0, -1)
                elif face == (0, -1):
                    face = (-1, 0)
                else:
                    face = (0, 1)
        return start, face


if __name__ == '__main__':
    sol = Solution()
    print(sol.isRobotBounded("GGLLGG"))



