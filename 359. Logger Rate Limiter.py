class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.mess = set()
        self.time = deque() # will store (time, message)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.time and timestamp - self.time[0][0] >= 10:
            t, me = self.time.popleft()
            self.mess.remove(me)
        if message not in self.mess:
            self.mess.add(message)
            self.time.append((timestamp, message))
            return True
        else:
            return False
