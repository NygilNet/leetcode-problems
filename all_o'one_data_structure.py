"""
link to leetcode: https://leetcode.com/problems/all-oone-data-structure/?envType=daily-question&envId=2024-09-29

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""

from collections import defaultdict
class AllOne:
    def __init__(self):
        self.counts = defaultdict(set)
        self.lookup = defaultdict(int)
        self.max_count = None
        self.min_count = None

    def inc(self, key: str) -> None:
        count = self.lookup[key] if key in self.lookup else 0
        new_count = count + 1
        if count:
            self.counts[count].remove(key)
            self.counts[new_count].add(key)
        else:
            self.lookup[key] += 1
            self.counts[1].add(key)
            
        if not self.max_count or new_count > self.max_count:
            self.max_count = new_count
            if not self.min_count:
                self.min_count = new_count

    def dec(self, key: str) -> None:
        count = self.lookup[key]
        self.counts[count].remove(key)
        if not self.counts[count]:
            del self.counts[count]
        if count == 1:
            del self.lookup[key]
        else:
            new_count = count - 1
            self.counts[new_count].add(key)
            self.lookup[key] = new_count
            if new_count < self.min_count:
                self.min_count = new_count
            if self.max_count == count and not self.counts[count]:
                self.max_count = new_count
        
        if not self.counts and not self.lookup:
            self.max_count = None
            self.min_count = None 
        
    def getMaxKey(self) -> str:
        if self.max_count and self.counts[self.max_count]:
            rand = self.counts[self.max_count].pop()
            self.counts[self.max_count].add(rand)
            return rand
        else:
            return ""

    def getMinKey(self) -> str:
        if self.min_count and self.counts[self.min_count]:
            rand = self.counts[self.min_count].pop()
            self.counts[self.min_count].add(rand)
            return rand
        else:
            return ""