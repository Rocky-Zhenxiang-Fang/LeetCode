class RandomizedSet:
    """
    Idea:
        We know that we need to use hashmap and list to get O(1) runtime
        map is not good for getting random item, so this will be leave to list
        list is not good for removing item in the middle, thus, we can first swap the item to the last, then remove it
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.value_index:
            self.value_index[val] = len(self.nums)
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.value_index:
            return False
        else:
            i = self.value_index[val]
            original = self.nums[-1]
            self.nums[-1], self.nums[i] = self.nums[i], self.nums[-1]
            self.nums.pop()
            self.value_index[original] = i
            self.value_index.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random as rand
        i = rand.randint(0, len(self.nums))
        return self.nums[i]
