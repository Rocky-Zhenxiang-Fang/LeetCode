import collections


class UndergroundSystem:

    def __init__(self):
        self.peoples = {}  # id: (start, time)
        self.averages = collections.defaultdict(default_factory=[0, 0])  # (start, end): [sum, num_of_tuples]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.peoples[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.peoples[id]
        del self.peoples[id]
        if (start, stationName) in self.averages:
            self.averages[(start, stationName)][0] += time - t
            self.averages[(start, stationName)][1] += 1
        else:
            self.averages[(start, stationName)] = [time - t, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        summation, num = self.averages[(startStation, endStation)]
        return summation / num
