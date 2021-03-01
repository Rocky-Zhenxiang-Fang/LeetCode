import collections
class FreqStack:
    """
    Idea:
        We care about the frequency of each element.
        We can keep a max_freq so that we can return the number that has this freq in constant time
        By keeping freq: index will not do since there can multiple index having the same freq
        Thus, we keep another map freq: [elements]. The value can also be used as a stack so it there is a tie, we
        only need to return the last number
    """
    def __init__(self):
        self.freq = collections.Counter()   # this is used to decide which group to add to
        self.groups = collections.defaultdict(list)     # this groups the elements that have the same occurs
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.groups[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])

    def pop(self) -> int:
        res = self.groups[self.max_freq].pop()
        self.freq[res] -= 1
        if len(self.groups[self.max_freq]) == 0:
            self.max_freq -= 1
        return res
