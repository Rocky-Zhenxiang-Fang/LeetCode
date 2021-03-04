from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Idea:
            Do DFS, if the cell has the same color, replace the color
        """
        original_color = image[sr][sc]
        if original_color == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            s = stack.pop()
            sr, sc = s[0], s[1]
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == original_color:
                image[sr][sc] = newColor
                for m in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    stack.append((sr + m[0], sc + m[1]))

        return image


if __name__ == '__main__':
    sol = Solution()
    im = [[0, 0, 0], [0, 1, 1]]
    r = 1
    c = 1
    col = 1
    print(sol.floodFill(im, r, c, col))
