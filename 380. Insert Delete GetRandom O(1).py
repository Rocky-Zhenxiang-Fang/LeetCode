class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randomSet:
            return False
        else:
            self.randomSet.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        randomList = list(self.randomSet)
        n = random.randint(0, len(randomList) - 1)
        return randomList[n]
