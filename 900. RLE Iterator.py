from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoded = encoding
        self.ptr = 0    # pointer to self.encoded
        self.exhaused = 0
        self.orignal_len = 0
        self.pre_len = encoding[0]

    def next(self, n: int) -> int:
        self.exhaused += n
        while self.exhaused > self.pre_len:
            self.ptr += 2
            if self.ptr >= len(self.encoded):
                return -1
            self.pre_len += self.encoded[self.ptr]
            
        return self.encoded[self.ptr + 1]
        

if __name__ == '__main__':
    rle = RLEIterator([3, 8, 0, 9, 2, 5])
    print(rle.next(2))
    print(rle.next(1))
    print(rle.next(1))
    print(rle.next(2))