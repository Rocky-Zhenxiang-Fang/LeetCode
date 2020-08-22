class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[None] for _ in range(8)]
        self.size = 0
        self.loadFactor = 0.0

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        if self.loadFactor > 0.75:
            self.resize(len(self.arr) * 2)
        i = key % len(self.arr)
        self.arr[i].append(key)
        self.size += 1
        self.loadFactor = self.size / len(self.arr)

    def remove(self, key: int) -> None:
        if self.loadFactor < 0.25:
            self.resize(len(self.arr) // 2)
        i = key % len(self.arr)
        for item in self.arr[i]:
            if item == key:
                self.arr[i].remove(item)
                self.size -= 1
                self.loadFactor = self.size / len(self.arr)
                break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = key % len(self.arr)
        for item in self.arr[i]:
            if item == key:
                return True
        return False

    def resize(self, capacity: int):
        """
        resize self.arr if the loadFactor is bigger then 0.75 or smaller the 0.25
        """
        newArr = [[None] for _ in range(capacity)]
        for i in range(len(self.arr)):
            for item in self.arr[i]:
                if not item:
                    continue
                j = item % capacity
                newArr[j].append(item)
        self.arr = newArr


if __name__ == '__main__':
    hashSet = MyHashSet()
    for i in range(10):
        hashSet.add(i)
    print("Done")