class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Create a list for the key if it doesn't exist
        if key not in self.map:
            self.map[key] = []

        # Store [value, timestamp] in increasing timestamp order
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, no value can be returned
        if key not in self.map:
            return ""

        left = 0
        right = len(self.map[key]) - 1

        # Stores the latest value with timestamp <= requested timestamp
        result = ""

        while left <= right:
            middle = (left + right) // 2
            middle_timestamp = self.map[key][middle][1]

            if middle_timestamp == timestamp:
                # Exact timestamp found
                return self.map[key][middle][0]

            elif middle_timestamp > timestamp:
                # Timestamp is too large, search the left half
                right = middle - 1

            else:
                # Valid timestamp, but there may be a newer valid one
                result = self.map[key][middle][0]
                left = middle + 1

        # Return the latest value found, or "" if none was valid
        return result