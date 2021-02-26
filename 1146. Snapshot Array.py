import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.nums = [[[0, 0]] for _ in range(length)]   # stores [snap_id, val]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.nums[index][-1][0] == self.snap_id: # if the last element is at the current snap_id, update
            self.nums[index][-1][1] = val
        else:
            self.nums[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        target = self.nums[snap_id]
        if snap_id >= target[-1][0]:
            return target[-1][1]
        elif snap_id == 0:
            return target[0][1]
        else:
            left, right = 0, len(target) - 1    # find a id that is target[mid][0] < id < target[mid + 1][0]
            while left <= right:
                mid = (left + right) // 2
                if target[mid][0] <= index < target[mid + 1][0]:
                    return target[mid][1]
                elif target[mid][0] > index:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1


if __name__ == '__main__':
    arr = SnapshotArray(3)
    arr.set(0, 5)
    print(arr.snap())
    arr.set(0, 6)
    print(arr.get(0, 0))