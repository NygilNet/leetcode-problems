"""

link to leetcode: https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

"""

class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def _inbounds(index, arr_length):
            return 0 <= index < arr_length   
        arr = self.pairs.get(key)
        if not arr:
            return ""
        left = 0
        right = len(arr)
        length = len(arr)
        while left <= right:
            mid = left + ((right - left) // 2)
            if not _inbounds(mid, length):
                break    
            prev_timestamp, val = arr[mid]
            if prev_timestamp == timestamp:
                return val
            if prev_timestamp < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return val if val and prev_timestamp < timestamp else ""
        