class TimeMap:

    def __init__(self):

        self.keyToTimes = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.keyToTimes:
            self.keyToTimes[key] = []
        self.keyToTimes[key].append( (timestamp, value))
        # always sorted by timestamp by order inserted
        

    def get(self, key: str, timestamp: int) -> str:

        # if it doesn't exist at all
        if key not in self.keyToTimes:
            return ""

        # if it exists
        timeAndValues = self.keyToTimes[key]
        i = 0
        j = len(timeAndValues) - 1
        result = ""

        while i <= j:
            mid = (i + j) // 2

            if timeAndValues[mid][0] <= timestamp:
                result = timeAndValues[mid][1]
                i = mid + 1
            else:
                j = mid - 1
        return result
        

        
