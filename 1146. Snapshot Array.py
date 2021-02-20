import bisect


class SnapshotArray:
    """
    Idea:
        Only store the changes
    """
    def __init__(self, length: int):
        self.values = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        """
        If the value has already been stored in the current snap shoot, update the value
        otherwise, append the value
        """
        if self.values[index][-1][0] == self.snap_id:
            self.values[index][-1][1] = val
        else:
            self.values[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        use BST to improve run time
        """
        i = bisect.bisect(self.values[index], [snap_id + 1, -float("inf")]) - 1     # +1 for selecting the right most value, -1 for picking the biggest smaller one
        return self.values[index][i][1]

if __name__ == '__main__':
    arr = SnapshotArray(3)
    arr.set(0, 5)
    print(arr.snap())
    arr.set(0, 6)
    print(arr.get(0, 0))