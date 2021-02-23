class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.size = size
        self.running_sum = 0
        self.que = deque()

    def next(self, val: int) -> float:
        self.running_sum += val
        self.que.append(val)
        if len(self.que) > self.size:
            self.running_sum -= self.que.popleft()
        return self.running_sum / len(self.que)


if __name__ == '__main__':
    mv = MovingAverage(3)
    print(mv.next(1))
    print(mv.next(10))
    print(mv.next(3))
    print(mv.next(5))
