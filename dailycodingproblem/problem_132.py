"""
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?
"""

import bisect
from datetime import datetime, timedelta

class HitCounter:
    def __init__(self) -> None:
        self.timestamps = []

    
    def record(self, timestamp: datetime) -> bool:
        insert_pos = bisect.bisect_left(self.timestamps, timestamp)
        if insert_pos == len(self.timestamps) or self.timestamps[insert_pos] != timestamp:
            self.timestamps.insert(insert_pos, timestamp)
        return True


    def total(self) -> int:
        return len(self.timestamps)
    

    def range(self, lower: datetime, upper: datetime) -> int:
        if lower > upper:
            raise ValueError("Lower bound must be less than or equal to upper bound")
        
        lower_index = bisect.bisect_left(self.timestamps, lower)
        upper_index = bisect.bisect_right(self.timestamps, upper)

        return upper_index - lower_index

# from datetime import datetime
# class HitCounter:
#     def __init__(self) -> None:
#         self.tracker = {}

    
#     def record(self, timestamp: datetime) -> bool:
#         self.tracker[timestamp] = len(self.tracker) + 1
#         return True



#     def total(self) -> int:
#         return len(self.tracker)
    

#     def range(self, lower: datetime, upper: datetime) -> int:
#         l, u = lower, upper

#         while l < u and (l not in self.tracker or u not in self.tracker):
#             if l not in self.tracker:
#                 l += datetime.second(1)
#             if u not in self.tracker:
#                 u -= datetime.second(1)
        
#         hits = self.tracker[u] if u in self.tracker and l not in self.tracker else self.tracker[l] if l in self.tracker and u not in self.tracker else self.tracker[u] - self.tracker[l]
#         return hits